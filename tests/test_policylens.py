from unittest.mock import Mock

import pytest
import policylens


@pytest.fixture
def app(monkeypatch):
    """Give every test fresh input fields, messages and result tables."""

    field_names = [
        'search_text',
        'from_date_inp',
        'to_date_inp',
        'document_type_inp',
        'burger_status',
        'research_status',
    ]

    for name in field_names:
        field = Mock()
        field.get.return_value = ''
        monkeypatch.setattr(policylens, name, field, raising=False)

    for name in ['burger_results', 'research_results']:
        table = Mock()
        table.get_children.return_value = ()
        monkeypatch.setattr(policylens, name, table, raising=False)

    monkeypatch.setattr(
        policylens,
        'load_mock_document',
        Mock(return_value=[]),
    )


    monkeypatch.setattr(policylens, 'research_documents', [])

    return policylens

@pytest.mark.parametrize('query', ['', '  ', 'a'])
def test_tp01_burger_rejects_short_input(app, query):
    # Arrange: choose the input
    app.search_text.get.return_value = query

    # Act: run the actual application function
    app.search_burger()

    # Assert: check the message and asence of a search
    app.burger_status.set.assert_called_once_with(
        'Vul minimaal twee tekens in.'
    )
    app.burger_results.insert.assert_not_called()
    app.load_mock_document.assert_not_called()

def test_tp02_burger_shows_ten_newest_results(app):
    # Arrange: 25 matching documents, initially oldest first
    app.search_text.get.return_value = 'privacy'
    app.load_mock_document.return_value = [
        document(str(day), f"2026-11-{day:02d}")
        for day in range(1, 26)
    ]

    # Act
    app.search_burger()

    # Read the rows that the application attempted to display
    rows = [
        call.kwargs['values']
        for call in app.burger_results.insert.call_args_list
    ]

    # Assert: ten rows, with the expected newest and oldest boundaries
    assert len(rows) == 10
    assert rows[0][1] == '2026-11-25'
    assert rows[-1][1] == '2026-11-16'


def test_tp06_research_filters_dates_and_document_type(app):
    # Arrange: the five records from test scenario
    app.load_mock_document.return_value = [
        document("A", "2026-11-09"),
        document("B", "2026-11-10"),
        document("C", "2026-11-20"),
        document("D", "2026-11-15", "Brief regering"),
        document("E", "2026-11-21"),
    ]

    app.search_text.get.return_value = "privacy"
    app.from_date_inp.get.return_value = "10-11-2026"
    app.to_date_inp.get.return_value = "20-11-2026"
    app.document_type_inp.get.return_value = "Motie"

    # Act.
    app.search_researcher()

    # Assert: both date boundaries are included, newest first.
    identifiers = [
        record["Id"] for record in app.research_documents
    ]

    assert identifiers == ["C", "B"]
    assert app.research_results.insert.call_count == 2


@pytest.mark.parametrize(
    "start, end, expected_message",
    [
        (
            "31-02-2026",
            "",
            "Gebruik geldige datums als dd-mm-jjjj.",
        ),
        (
            "20-11-2026",
            "10-11-2026",
            "Vanaf datum mag niet na Tot datum liggen",
        ),
    ],
)
def test_tp06_research_rejects_invalid_dates(
    app, start, end, expected_message
):
    # Arrange.
    app.search_text.get.return_value = "privacy"
    app.from_date_inp.get.return_value = start
    app.to_date_inp.get.return_value = end

    # Act.
    app.search_researcher()

    # Assert.
    app.research_status.set.assert_called_once_with(
        expected_message
    )
    app.load_mock_document.assert_not_called()
    assert app.research_documents == []


def test_tp11_burger_handles_no_matching_documents(app):
    # Arrange: a valid search term that does not match the supplied document.
    app.search_text.get.return_value = "volcano"
    app.load_mock_document.return_value = [document("A", "2026-11-20")]
    app.burger_results.get_children.return_value = ("previous-result",)

    # Act.
    app.search_burger()

    # Assert: clear old results, show the empty-result message and keep input.
    app.load_mock_document.assert_called_once_with()
    app.burger_results.delete.assert_called_once_with("previous-result")
    app.burger_results.insert.assert_not_called()
    app.burger_status.set.assert_called_once_with("Geen documenten gevonden.")
    app.search_text.set.assert_not_called()


def test_tp11_research_handles_no_matching_documents(app):
    # Arrange: include old results to check that the new search clears them.
    app.search_text.get.return_value = "volcano"
    app.load_mock_document.return_value = [document("A", "2026-11-20")]
    app.research_documents.append(document("previous", "2026-11-19"))
    previous_rows = ["previous-result"]
    app.research_results.get_children.side_effect = lambda: tuple(previous_rows)
    app.research_results.delete.side_effect = previous_rows.remove

    # Act.
    app.search_researcher()

    # Assert: no stale records remain and the message explains the empty set.
    app.load_mock_document.assert_called_once_with()
    assert app.research_documents == []
    app.research_results.delete.assert_called_once_with("previous-result")
    app.research_results.insert.assert_not_called()
    app.research_status.set.assert_called_once()
    message = app.research_status.set.call_args.args[0]
    assert message.startswith("Geen documenten")
    assert message.endswith("met deze zoekterm en filters.")
    app.search_text.set.assert_not_called()


def test_load_corrupt_database_shows_message(app, tmp_path, monkeypatch):
    # L-02: gebruik een tijdelijk bestand zodat echte opgeslagen data intact blijft.
    database_path = tmp_path / "broken.json"
    database_path.write_text("{broken", encoding="utf-8")
    monkeypatch.setattr(app, "DATABASE_FILE", database_path)
    previous_document = document("previous", "2026-11-19")
    app.research_documents.append(previous_document)

    app.load_research_results()

    # Een leesfout mag de oude resultaten en het bronbestand niet vervangen.
    app.research_status.set.assert_called_once_with(
        "Lokale opslag kon niet worden gelezen."
    )
    app.research_results.delete.assert_not_called()
    app.research_results.insert.assert_not_called()
    assert app.research_documents == [previous_document]
    assert database_path.read_text(encoding="utf-8") == "{broken"


def document(identifier, date, kind="Motie"):
    """Create one predictable test document."""
    return {
        "Id": identifier,
        "Titel": f"Privacy document {identifier}",
        "Onderwerp": "Persoonsgegevens",
        "Datum": date,
        "Soort": kind,
        "Verwijderd": "false",
    }

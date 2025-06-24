from unittest.mock import patch, Mock
from task2.solution import parse_page


def test_parse_page_returns_expected_data():
    html = """
    <div id="mw-pages">
        <div class="mw-category-group">
            <h3>А</h3>
            <ul>
                <li><a href="/wiki/Аист">Аист</a></li>
                <li><a href="/wiki/Акула">Акула</a></li>
            </ul>
        </div>
        <a href="/next_page_url">Следующая страница</a>
    </div>
    """
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = html
    with patch("requests.get", return_value=mock_response):
        next_url, result = parse_page("/fake_url")
    assert next_url == "/next_page_url"
    assert result == {"А": 2}


def test_parse_page_multiple_letters():
    html = """
    <div id="mw-pages">
        <div class="mw-category-group">
            <h3>В</h3>
            <ul>
                <li><a href="/wiki/Воробей">Воробей</a></li>
            </ul>
        </div>
        <div class="mw-category-group">
            <h3>Г</h3>
            <ul>
                <li><a href="/wiki/Гусь">Гусь</a></li>
                <li><a href="/wiki/Гадюка">Гадюка</a></li>
            </ul>
        </div>
        <a href="/next">Следующая страница</a>
    </div>
    """
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = html
    with patch("requests.get", return_value=mock_response):
        next_url, result = parse_page("/fake_url")
    assert next_url == "/next"
    assert result == {"В": 1, "Г": 2}


def test_parse_page_no_next_page():
    html = """
    <div id="mw-pages">
        <div class="mw-category-group">
            <h3>Д</h3>
            <ul>
                <li><a href="/wiki/Дельфин">Дельфин</a></li>
            </ul>
        </div>
    </div>
    """
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = html
    with patch("requests.get", return_value=mock_response):
        next_url, result = parse_page("/fake_url")
    assert next_url is None
    assert result == {"Д": 1}

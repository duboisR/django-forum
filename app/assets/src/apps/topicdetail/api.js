// Constants
const _getCookie = (name) => {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].replace(/^\s+|\s+$/g, "");
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const _getJsonHeader = () => {
    return {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-CSRFToken': _getCookie('csrftoken'),
    }
}

const jsonFetchData = (url, method = 'GET', data = null) => {
    const body = data == null ? null : JSON.stringify(data);
    const init = { method, body, headers: _getJsonHeader(), credentials: 'same-origin' };
    return fetch(url, init).then(response => response.json());
}

export default jsonFetchData
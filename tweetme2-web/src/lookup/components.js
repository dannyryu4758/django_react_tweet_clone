function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

export function backendLookup(method, endpoint, callback, data) {
  let jsonData;
  if (data) {
    jsonData = JSON.stringify(data);
  }
  const xhr = new XMLHttpRequest(); // xhr = SomeClass()
  const url = `http://localhost:8000/api${endpoint}`;
  xhr.responseType = "json";
  const csrftoken = getCookie("csrftoken");
  xhr.open(method, url);
  xhr.setRequestHeader("Content-Type", "application/json");

  if (csrftoken) {
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest"); // ajax 를 사용하기 위한 세팅1
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest"); // ajax 를 사용하기 위한 세팅2
    xhr.setRequestHeader("X-CSRFToken", csrftoken); // ajax Cross Site Request Forgery protection
  }

  xhr.onload = function () {
    if (xhr.status === 403) {
      const detail = xhr.response.detail;
      if (
        detail ===
        "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."
      ) {
        window.location.href = "/login?showLoginRequired=true";
      }
    }
    callback(xhr.response, xhr.status);
  };
  xhr.onerror = function (e) {
    // console.log("error", e);
    callback({ message: "해당 요청은 오류가 있습니다." }, 400);
  };
  xhr.send(jsonData);
}

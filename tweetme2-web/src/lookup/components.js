import React from "react";

export function loadTweets(callback) {
    const xhr = new XMLHttpRequest() // xhr = SomeClass()
    const method = 'GET' // "POST"
    const url = 'http://localhost:8000/api/tweets/'
    const responseType = 'json'
    xhr.responseType = responseType
    xhr.open(method, url) 
    xhr.onload = function() {
        callback(xhr.response, xhr.status)
    }
    xhr.onerror = function(e) {
        console.log(e)
        callback({'message':'해당 요청은 오류가 있습니다.'}, 400)
    }
    xhr.send()
}
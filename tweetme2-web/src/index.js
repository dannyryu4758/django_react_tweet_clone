import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import { TweetsComponent } from "./tweets";
import reportWebVitals from "./reportWebVitals";

const appEl = document.getElementById("root");
if (appEl) {
  ReactDOM.render(<App />, appEl);
}

const e = React.createElement;
const tweetEl = document.getElementById("tweetme-2");
if (tweetEl) {
  console.log(tweetEl.dataset);
  ReactDOM.render(e(TweetsComponent, tweetEl.dataset), tweetEl);
}

// ReactDOM.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
//   document.getElementById('root')
// );

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

(this["webpackJsonptweetme2-web"]=this["webpackJsonptweetme2-web"]||[]).push([[0],{14:function(e,t,n){},15:function(e,t,n){},17:function(e,t,n){"use strict";n.r(t);var c=n(1),a=n.n(c),s=n(6),r=n.n(s),o=(n(14),n.p+"static/media/logo.6ce24c58.svg");n(15);function i(e,t,n,c){var a;c&&(a=JSON.stringify(c));var s=new XMLHttpRequest,r="http://localhost:8000/api".concat(t);s.responseType="json";var o=function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),c=0;c<n.length;c++){var a=n[c].trim();if(a.substring(0,e.length+1)===e+"="){t=decodeURIComponent(a.substring(e.length+1));break}}return t}("csrftoken");s.open(e,r),s.setRequestHeader("Content-Type","application/json"),o&&(s.setRequestHeader("HTTP_X_REQUESTED_WITH","XMLHttpRequest"),s.setRequestHeader("X-Requested-With","XMLHttpRequest"),s.setRequestHeader("X-CSRFToken",o)),s.onload=function(){403===s.status&&("\uc790\uaca9 \uc778\uc99d\ub370\uc774\ud130(authentication credentials)\uac00 \uc81c\uacf5\ub418\uc9c0 \uc54a\uc558\uc2b5\ub2c8\ub2e4."===s.response.detail&&(window.location.href="/login?showLoginRequired=true"));n(s.response,s.status)},s.onerror=function(e){n({message:"\ud574\ub2f9 \uc694\uccad\uc740 \uc624\ub958\uac00 \uc788\uc2b5\ub2c8\ub2e4."},400)},s.send(a)}var l=n(0);function u(e){var t=e.tweet,n=e.action,c=e.didPerformAction,a=t.likes?t.likes:0,s=e.className?e.className:"btn btn-primary btn-sm",r=n.display?n.display:"Action",o=function(e,t){console.log(e,t),200!==t&&201!==t||!c||c(e,t)},u="like"===n.type?"".concat(a," ").concat(r):r;return Object(l.jsx)("button",{className:s,onClick:function(e){e.preventDefault(),function(e,t,n){i("POST","/tweets/action/",n,{id:e,action:t})}(t.id,n.type,o)},children:u})}var d=n(3),j=n(2),b=n(8);function m(e){var t=e.tweet;return t.parent?Object(l.jsx)("div",{className:"row",children:Object(l.jsxs)("div",{className:"col-11 mx-auto p-3 border rounded",children:[Object(l.jsx)("p",{className:"mb-0 text-muted small",children:"Retweet"}),Object(l.jsx)(f,{hideActions:!0,className:" ",tweet:t.parent})]})}):null}function f(e){var t=e.tweet,n=e.didRetweet,s=e.hideActions,r=Object(c.useState)(e.tweet?e.tweet:null),o=Object(j.a)(r,2),i=o[0],d=o[1],f=e.className?e.className:"col-10 mx-auto col-md-6",p=window.location.pathname,O=Object(b.a)(/([0-9]+)/,{tweetid:1}),w=p.match(O),h=w?w.groups.tweetid:-1,v="".concat(t.id)==="".concat(h),x=function(e,t){200===t?d(e):201===t&&n&&n(e)};return Object(l.jsxs)("div",{className:f,children:[Object(l.jsxs)("div",{children:[Object(l.jsxs)("p",{children:[t.id," - ",t.content]}),Object(l.jsx)(m,{tweet:t})]}),Object(l.jsxs)("div",{className:"btn btn-group",children:[i&&!0!==s&&Object(l.jsxs)(a.a.Fragment,{children:[Object(l.jsx)(u,{tweet:i,didPerformAction:x,action:{type:"like",display:"Likes"}}),Object(l.jsx)(u,{tweet:i,didPerformAction:x,action:{type:"unlike",display:"Unlike"}}),Object(l.jsx)(u,{tweet:i,didPerformAction:x,action:{type:"retweet",display:"Retweet"}})]}),!0===v?null:Object(l.jsx)("button",{className:"btn btn-outline-primary btn-sm",onClick:function(e){e.preventDefault(),window.location.href="/".concat(t.id)},children:"View"})]})]})}function p(e){var t=Object(c.useState)([]),n=Object(j.a)(t,2),a=n[0],s=n[1],r=Object(c.useState)([]),o=Object(j.a)(r,2),u=o[0],b=o[1],m=Object(c.useState)(!1),p=Object(j.a)(m,2),O=p[0],w=p[1];Object(c.useEffect)((function(){var t=Object(d.a)(e.newTweets).concat(a);t.length!==u.length&&b(t)}),[e.newTweets,u,a]),Object(c.useEffect)((function(){if(!1===O){!function(e,t){var n="/tweets/";e&&(n="/tweets/?username=".concat(e)),i("GET",n,t)}(e.username,(function(e,t){200===t?(s(e),w(!0)):alert("\uc624\ub958\uac00 \uc788\uc2b5\ub2c8\ub2e4.")}))}}),[a,O,w,e.username]);var h=function(e){var t=Object(d.a)(a);t.unshift(e),s(t);var n=Object(d.a)(u);n.unshift(u),b(n)};return u.map((function(e,t){return Object(l.jsx)(f,{tweet:e,didRetweet:h,className:"my-5 py-5 border bg-white text-dark"},"".concat(t,"-{item.id}"))}))}var O=n(9);function w(e){var t=a.a.createRef(),n=e.didTweet,c=function(e,t){201===t?n(e):(console.log(e),alert("\uc624\ub958\uac00 \ubc1c\uc0dd\ud588\uc2b5\ub2c8\ub2e4. \ub2e4\uc2dc \uc2dc\ub3c4\ud558\uc138\uc694."))};return Object(l.jsx)("div",{className:e.className,children:Object(l.jsxs)("form",{onSubmit:function(e){e.preventDefault();var n=t.current.value;i("POST","/tweets/create/",c,{content:n}),t.current.value=""},children:[Object(l.jsx)("textarea",{ref:t,required:!0,className:"form-control",name:"tweet"}),Object(l.jsx)("button",{type:"submit",className:"btn btn-primary my-3",children:"Tweet"})]})})}function h(e){var t=Object(c.useState)([]),n=Object(j.a)(t,2),a=n[0],s=n[1],r="false"!==e.canTweet;console.log(!1===r);return Object(l.jsxs)("div",{className:e.className,children:[!0===r&&Object(l.jsx)(w,{didTweet:function(e){var t=Object(d.a)(a);t.unshift(e),s(t)},className:"col-12 mb-3"}),Object(l.jsx)(p,Object(O.a)({newTweets:a},e))]})}function v(e){var t=e.tweetId,n=Object(c.useState)(!1),a=Object(j.a)(n,2),s=a[0],r=a[1],o=Object(c.useState)(null),u=Object(j.a)(o,2),d=u[0],b=u[1],m=function(e,t){200===t?b(e):alert("\ud574\ub2f9 \ud2b8\uc717\uc744 \ucc3e\ub294 \ub3c4\uc911 \uc624\ub958\uac00 \ubc1c\uc0dd\ud558\uc600\uc2b5\ub2c8\ub2e4.")};return Object(c.useEffect)((function(){!1===s&&(!function(e,t){i("GET","/tweets/".concat(e,"/"),t)}(t,m),r(!0))}),[t,s,r]),null===d?null:Object(l.jsx)(f,{tweet:d,className:e.className})}var x=function(){return Object(l.jsx)("div",{className:"App",children:Object(l.jsxs)("header",{className:"App-header",children:[Object(l.jsx)("img",{src:o,className:"App-logo",alt:"logo"}),Object(l.jsxs)("p",{children:["Edit ",Object(l.jsx)("code",{children:"src/App.js"})," and save to reload."]}),Object(l.jsx)("div",{children:Object(l.jsx)(h,{})}),Object(l.jsx)("a",{className:"App-link",href:"https://reactjs.org",target:"_blank",rel:"noopener noreferrer",children:"Learn React"})]})})},g=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,18)).then((function(t){var n=t.getCLS,c=t.getFID,a=t.getFCP,s=t.getLCP,r=t.getTTFB;n(e),c(e),a(e),s(e),r(e)}))},N=document.getElementById("root");N&&r.a.render(Object(l.jsx)(x,{}),N);var y=a.a.createElement,k=document.getElementById("tweetme-2");k&&(console.log(k.dataset),r.a.render(y(h,k.dataset),k)),document.querySelectorAll(".tweetme-2-detail").forEach((function(e){r.a.render(y(v,e.dataset),e)})),g()}},[[17,1,2]]]);
//# sourceMappingURL=main.3b555ef3.chunk.js.map
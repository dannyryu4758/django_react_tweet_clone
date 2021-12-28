import React from "react";
import { apiTweetCreate } from "./lookup";

export function TweetCreate(props) {
  const textAreaRef = React.createRef();
  const { didTweet } = props;
  const handleBackendUpdate = (response, status) => {
    // backend api response handler
    if (status === 201) {
      didTweet(response);
    } else {
      console.log(response);
      alert("오류가 발생했습니다. 다시 시도하세요.");
    }
  };

  const handleSubmit = (event) => {
    // backend api request
    event.preventDefault();
    const newVal = textAreaRef.current.value;
    apiTweetCreate(newVal, handleBackendUpdate);
    textAreaRef.current.value = "";
  };
  return (
    <div className={props.className}>
      <form onSubmit={handleSubmit}>
        <textarea
          ref={textAreaRef}
          required={true}
          className="form-control"
          name="tweet"
        ></textarea>
        <button type="submit" className="btn btn-primary my-3">
          Tweet
        </button>
      </form>
    </div>
  );
}

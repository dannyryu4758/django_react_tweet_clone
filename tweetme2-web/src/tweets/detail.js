import React, { useState } from "react";
import { ActionBtn } from "./button";
import { ParentTweet } from "./components";

export function Tweet(props) {
  const { tweet, didRetweet, hideActions } = props;
  const [actionTweet, setActionTweet] = useState(
    props.tweet ? props.tweet : null
  );
  const className = props.className
    ? props.className
    : "col-10 mx-auto col-md-6";

  const handlePerformAction = (newActionTweet, status) => {
    if (status === 200) {
      setActionTweet(newActionTweet);
    } else if (status === 201) {
      if (didRetweet) {
        didRetweet(newActionTweet);
      }
    }
  };

  return (
    <div className={className}>
      <div>
        <p>
          {tweet.id} - {tweet.content}
        </p>
        <ParentTweet tweet={tweet} />
      </div>
      {actionTweet && hideActions !== true && (
        <div className="btn btn-group">
          <ActionBtn
            tweet={actionTweet}
            didPerformAction={handlePerformAction}
            action={{ type: "like", display: "Likes" }}
          />
          <ActionBtn
            tweet={actionTweet}
            didPerformAction={handlePerformAction}
            action={{ type: "unlike", display: "Unlike" }}
          />
          <ActionBtn
            tweet={actionTweet}
            didPerformAction={handlePerformAction}
            action={{ type: "retweet", display: "Retweet" }}
          />
        </div>
      )}
    </div>
  );
}

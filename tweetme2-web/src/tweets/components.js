import React, { useState, useEffect } from "react";
import { TweetsList } from "./list";
import { TweetCreate } from "./create";
import { apiTweeDetail } from "./lookup";
import { Tweet } from "./detail";

export function TweetsComponent(props) {
  const [newTweets, setNewTweets] = useState([]);
  const canTweet = props.canTweet === "false" ? false : true;
  console.log(canTweet === false);
  const handleNewTweet = (newTweet) => {
    let tempNewTweets = [...newTweets];
    tempNewTweets.unshift(newTweet);
    setNewTweets(tempNewTweets);
  };

  return (
    <div className={props.className}>
      {canTweet === true && (
        <TweetCreate didTweet={handleNewTweet} className="col-12 mb-3" />
      )}
      <TweetsList newTweets={newTweets} {...props} />
    </div>
  );
}

export function TweetDetailComponent(props) {
  const { tweetId } = props;
  const [didLookup, setDidLookup] = useState(false);
  const [tweet, setTweet] = useState(null);
  const handleBackendLookup = (response, status) => {
    if (status === 200) {
      setTweet(response);
    } else {
      alert("해당 트윗을 찾는 도중 오류가 발생하였습니다.");
    }
  };
  useEffect(() => {
    if (didLookup === false) {
      apiTweeDetail(tweetId, handleBackendLookup);
      setDidLookup(true);
    }
  }, [tweetId, didLookup, setDidLookup]);
  return tweet === null ? null : (
    <Tweet tweet={tweet} className={props.className} />
  );
}

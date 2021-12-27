import React, { useEffect, useState } from "react";
import { createTweet, loadTweets } from "../lookup";

export function TweetsComponent(props) {
  const textAreaRef = React.createRef();
  const [newTweets, setNewTweets] = useState([]);
  const handleSubmit = (event) => {
    event.preventDefault();
    const newVal = textAreaRef.current.value;
    let tempNewTweets = [...newTweets];
    // 서버에서 데이터 불러오는 방식으로 변경 예정
    createTweet(newVal, (response, status) => {
      if (status === 201) {
        tempNewTweets.unshift(response);
      } else {
        console.log(response);
        alert("오류가 발생했습니다. 다시 시도하세요.");
      }
    });
    // tempNewTweets.unshift({ content: newVal, likes: 0, id: 12312 });
    setNewTweets(tempNewTweets);
    textAreaRef.current.value = "";
  };
  return (
    <div className={props.className}>
      <div className="col-12">
        <form onSubmit={handleSubmit}>
          <textarea
            ref={textAreaRef}
            required={true}
            className="form-control m-2"
          ></textarea>
          <button type="submit" className="btn btn-primary my-3">
            Tweet
          </button>
        </form>
      </div>
      <TweetsList newTweets={newTweets} />
    </div>
  );
}

export function TweetsList(props) {
  const [tweetsInit, setTweetsInit] = useState([]);
  const [tweets, setTweets] = useState([]);
  const [tweetsDidSet, setTweetsDidSet] = useState(false);
  useEffect(() => {
    let final = [...props.newTweets].concat(tweetsInit);
    if (final.length !== tweets.length) {
      setTweets(final);
    }
  }, [props.newTweets, tweets, tweetsInit]);

  useEffect(() => {
    if (tweetsDidSet === false) {
      const myCallback = (response, status) => {
        if (status === 200) {
          setTweetsInit(response);
          setTweetsDidSet(true);
        } else {
          alert("오류가 있습니다.");
        }
      };
      loadTweets(myCallback);
    }
  }, [tweetsInit, tweetsDidSet, setTweetsDidSet]);
  return tweets.map((item, index) => {
    return (
      <Tweet
        tweet={item}
        className="my-5 py-5 border bg-white text-dark"
        key={`${index}-{item.id}`}
      />
    );
  });
}

export function ActionBtn(props) {
  const { tweet, action } = props;
  const [likes, setLikes] = useState(tweet.likes ? tweet.likes : 0);
  const [userLike, setUserLike] = useState(
    tweet.userLike === true ? true : false
  );
  const className = props.className
    ? props.className
    : "btn btn-primary btn-sm";
  const actionDisplay = action.display ? action.display : "Action";
  const handleClick = (event) => {
    event.preventDefault();
    if (action.type === "like") {
      if (userLike === true) {
        // perhaps i Unlike it?
        setLikes(likes - 1);
        setUserLike(false);
      } else {
        setLikes(likes + 1);
        setUserLike(true);
      }
    }
  };
  const display =
    action.type === "like" ? `${likes} ${actionDisplay}` : actionDisplay;
  return (
    <button onClick={handleClick} className={className}>
      {display}
    </button>
  );
}

export function Tweet(props) {
  const { tweet } = props;
  const className = props.className
    ? props.className
    : "col-10 mx-auto col-md-6";
  return (
    <div className={className}>
      <p>
        {tweet.id} - {tweet.content}
      </p>
      <div className="btn btn-group">
        <ActionBtn tweet={tweet} action={{ type: "like", display: "Likes" }} />
        <ActionBtn
          tweet={tweet}
          action={{ type: "unlike", display: "Unlike" }}
        />
        <ActionBtn
          tweet={tweet}
          action={{ type: "retweet", display: "Retweet" }}
        />
      </div>
    </div>
  );
}

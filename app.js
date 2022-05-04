function _all(q, e=document){return e.querySelectorAll(q)}
function _one(q, e=document){return e.querySelector(q)}



function toggleTweetEditModal(){
  _one("#tweetEditModal").classList.toggle("hidden")
}

function toggleTweetModal(){
  _one("#tweetModal").classList.toggle("hidden")
}
// store the id of tweet that is meant to be updated
let current_update_tweet_id;
let user_data;

async function sendTweet(){
  const form = event.target
  // Get the button, set the data-await, and disable it
  const button = _one("button[type='submit']", form)
  console.log(button)
  button.innerText = button.dataset.await

  button.disabled = true
  const connection = await fetch("/api-create-tweet", {
    method : "POST",
    body : new FormData(form)
  })

  const tweet_info = await connection.text() // tweet id will be here
  console.log(tweet_info)
 const tweet_id = tweet_info;


 // get info about the user to display it in the tweet - names, username, profile picture
  getInfo('/user-info', 'GET', true)
  .then(data => {
    console.log(data) // JSON data parsed by `data.json()` call
    user_data = data;
    addTweet(data);
  });


  button.disabled = false
  button.innerText = button.dataset.default

  if( ! connection.ok ){
    console.log("connection issue")
    return
  }


function addTweet(data) {
console.log(_one("#tweet_image").value)
 let tweet_image = '';
  if (_one("#tweet_image").value) {
    full_image_src = _one("#tweet_image").value.substr(12)
    last_dot_index = full_image_src.lastIndexOf('.');
    console.log(last_dot_index)
    image_name = full_image_src.slice(0, last_dot_index);
    tweet_image =  `<img class="mt-2 w-full object-cover h-80" src="/images/${image_name}.jpeg">`
  }

  if (_one("#tweet_image2").value) {
    full_image_src = _one("#tweet_image2").value.substr(12)
    last_dot_index = full_image_src.lastIndexOf('.');
    console.log(last_dot_index)
    image_name = full_image_src.slice(0, last_dot_index);
    tweet_image =  `<img class="mt-2 w-full object-cover h-80" src="/images/${image_name}.jpeg">`
  }
  let tweet = `
    <div id="${tweet_id}" class="p-4 border-t border-slate-200">
    <div class="flex">
      <img class="flex-none w-12 h-12 rounded-full object-cover" src="/images/${data.user_info.pic}" alt="">
      <div class="w-full pl-4">
        <p class="font-bold">
          ${data.user_info.firstname} ${data.user_info.lastname}
        </p>            
        <p class="font-thin">
          @${data.user_info.name}
        </p>            
        <div class="pt-2 tweet-text">
          ${_one("input", form).value}
        </div>` + tweet_image +
        `<div class="flex gap-12 w-full mt-4 text-lg">
            <i onclick="delete_tweet('${tweet_id}')" class="fas fa-trash ml-auto"></i>
            <i class="fa-solid fa-message"></i>
            <i class="fa-solid fa-heart"></i>
            <i class="fa-solid fa-retweet"></i>
            <i class="fa-solid fa-share-nodes"></i>
            <i id="edit${tweet_id}" class="fa-solid fa-pen-to-square" onclick="getTweetId(
              event)"></i>
        </div>
      </div>
    </div>
  </div> 
  `
  _one("input", form).value = ""  

  if (!_one("#no-tweets-info").classList.contains("hidden")) {
    _one("#no-tweets-info").classList.add("hidden");
  }

  if (!_one("#tweetModal").classList.contains("hidden")) {
    _one("#tweetModal").classList.add("hidden")
  }

  _one("#tweets").insertAdjacentHTML("afterbegin", tweet)
};

}

// deleting the tweet
async function delete_tweet(tweet_id){
  console.log(tweet_id)
  // Connect to the api and delete it from the "database"
  const connection = await fetch(`/api-delete-tweet/${tweet_id}`, {
    method : "DELETE"
  })
  if( ! connection.ok ){
    alert("there has been a connection issue. Try again")
    return
  }
  document.querySelector(`[id='${tweet_id}']`).remove();
}

// get id of the tweet for an update
function getTweetId(event) {
  const tweet_id = event.target.id.slice(4);
  getInfo('/tweets', 'GET', true)
  .then(data => {
    // call function that gets the current tweet text
    getCurrentTweetInfo(data, tweet_id) 
  });
_one("#tweetEditModal").classList.toggle("hidden");
}




// reusable fetch 
async function getInfo(url, method, isjson) {
  const response = await fetch(url, {
    method: method, 
  });
  console.log(response)
  if (response.status == 200) {
  if  (isjson) {
  return response.json(); 
  } else {
    return response;
  }
} else {
  console.log("Check your connection - status: " + response.status)
}
}

// function related to updating the tweet 
function getCurrentTweetInfo(data, id) {
  //data.tweets.map(findTweetText)
  console.log(id)
  // set global variable to id of the tweet being currently updated
  current_update_tweet_id = id;

// get tweet index
  const tweet_index = data.tweets.findIndex(tweet => tweet.id === id)

// get the current text of the tweet
  _one("#tweet_edit_text").value = data.tweets[tweet_index].text;

  
}

// update the tweet - put route
function updateTweet() {
  const new_tweet_text = _one("#tweet_edit_text").value;

  getInfo(`/api-update-tweet/${current_update_tweet_id}/${new_tweet_text}`, 'PUT', false)
  .then(data => {
    console.log(data)
    if (data.status == 200) {
    _one(`#${CSS.escape(current_update_tweet_id)} .tweet-text`).textContent = new_tweet_text; }
    _one("#tweetEditModal").classList.add("hidden");// JSON data parsed by `data.json()` call
  });
}

// manage the followed users
function addFollowing(event) {
  const following_id = event.target.id;
  console.log(event.target.innerText)
  // if we want to follow the user - following route
  if (event.target.innerText == "Follow") {
  getInfo(`/follow-user/${following_id}`, 'POST', false)
  .then(data => {
    console.log(data)
    console.log("hi")
    event.target.innerText = "Following";
}); } else {
  // if we want to unfollow - unfollow route
  getInfo(`/unfollow-user/${following_id}`, 'DELETE', false)
  .then(data => {
    console.log(data)
    event.target.innerText = "Follow";
});
}
}


// display the user profile from right aside 
function getUserProfile(event) {
  const user_id = event.target.id.slice(4);

  getInfo(`/user-profile-info/${user_id}`, 'GET',  true)
  .then(userInfo => {
    console.log(userInfo)
    showUserProfile(userInfo)
});

getInfo(`/user-tweets/${user_id}`, 'GET',  true) 
.then(userInfo => {
  console.log(userInfo)
  userInfo = userInfo.tweets
  showUserTweets(userInfo, true)
});
}


// html for the user profile - inserting and removing it in order to avoid having to open a new page/refresh
function showUserProfile(user) {
let userProfile = `

<div class="p-3">
<i class="fa-solid fa-arrow-left" onclick={hideProfile()}></i>
${user.title}</div>
<img src="/images/twitter_bg_small.png" class="w-full" />
<div class="flex ml-6 -mt-8">
    <img src="/images/${user.img}" class="rounded-full -mt-8 h-32 w-32 object-cover">		
</div>
<div class="px-3 pb-6 pt-2">
<h2 class="text-white text-lg bold font-sans font-bold">${user.title}</h2>
<p class="font-light text-lightgrey">@${user.user_name}</p>
<p class="mt-2 font-sans font-light text-white">Hello, i'm from another the other side!</p>
</div>
<div class="flex px-3 text-white">
  <div class="text-center mr-3 pr-3">
    <p class="text-lightgrey"><span class="text-white">399</span> Following</p>
  </div>
  <div class="text-center">
    <p class="text-lightgrey"><span class="text-white">127K</span> Followers</p>
  </div>
</div>
`
console.log(_one("#user-profile"))
_one("#user-profile").innerHTML = "";
_one("#user-profile").insertAdjacentHTML("afterbegin", userProfile)
}

// get tweets for the user profile
function showUserTweets(tweets, hideInput, isAdmin) {
  
    _one("#tweets").innerHTML = "";


  if (hideInput) {_one("#add-tweet").classList.add("hidden")};
  tweets.forEach((tweet) => {
    console.log(tweet)
    let tweet_image = '';
    let edit_options = '';
    if (tweet.image) {
      tweet_image =  `<img class="mt-2 w-full object-cover h-80" src="/images/${tweet.image}">`
    }

    if ( user_data && (tweet.user_id) == user_data.user_info.id || isAdmin) {
      edit_options = `<i onclick="delete_tweet('${tweet.id}')" class="fas fa-trash"></i> <i id="edit${tweet.id}" class="fa-solid fa-pen-to-square" onclick="getTweetId(
        event)"></i>`
    }




    let oneTweet = `<div class="p-4 border-t border-mediumgrey"  id="${tweet.id}">
    <div class="flex">
    <img class="flex-none w-12 h-12 rounded-full object-cover" src="/images/${tweet.user_id}.jpeg" alt="">
      <div class="w-full pl-4">
        <p class="font-bold">
          ${tweet.user_firstname} ${tweet.user_lastname}
        </p>            
        <p class="font-thin">
          @${tweet.user_name}
        </p>            
        <div class="pt-2 tweet-text">
          ${tweet.text}
        </div>` + tweet_image + 

        `<div class="flex gap-12 w-full mt-4 text-lg">
          
            <i class="fa-solid fa-message ml-auto"></i>
            <i class="fa-solid fa-heart"></i>
            <i class="fa-solid fa-retweet"></i>
            <i class="fa-solid fa-share-nodes"></i>` + edit_options + 
           
        `</div>
      </div>
    </div>
  </div>`
  _one("#tweets").insertAdjacentHTML("afterbegin", oneTweet)
  })

} 

// admin panel function - switch from user to admin and back
function switchMode(event) {
  let isAdmin;
if (event.target.innerText == "Admin") {
  event.target.innerText = "User"
  isAdmin = true;
  getInfo(`/tweets`, 'GET',  true) 
  .then(tweets => {
    showUserTweets(tweets.tweets, false, isAdmin)
    _one("#add-tweet").classList.remove("hidden")
  });

} else {
  event.target.innerText = "Admin";
  isAdmin = false;
  getInfo(`/tweets`, 'GET',  true) 
.then(tweets => {
  showUserTweets(tweets.tweets, false, isAdmin)
});
 
}
}


// fetch all tweets and call search function
function getTweets() {
console.log()


getInfo(`/tweets`, 'GET',  true) 
.then(tweets => {
  console.log(tweets)
  let searchResults = [];
  searchTweets(tweets, searchResults)
});
}

// search function for tweet text
function searchTweets(tweets, searchResults) { 
  const searchQuery = _one("#search").value.toLowerCase();
  

  tweets.tweets.forEach((tweet) => {
    if (tweet.text.toLowerCase().includes(searchQuery)){
      searchResults.push(tweet)
      console.log(searchResults)
      
    } })
    if (searchResults[0]) {

      showUserTweets(searchResults, false) }
  }

  // go back to home page when clicking on back arrow in user profile
  function hideProfile() {
    _one("#user-profile").innerHTML = "";
    getInfo(`/tweets`, 'GET',  true) 
.then(tweets => {
  showUserTweets(tweets.tweets, false)
  if (!_one("#no-tweets-info").classList.contains("hidden")) {
    _one("#no-tweets-info").classList.add("hidden");
  }
  _one("#add-tweet").classList.remove("hidden")
});
  }

//fetch the user info to display only user's tweets
  function fetchMyInfo(){

    getInfo('/user-info', 'GET', true)
    .then(data => {
      console.log(data) // JSON data parsed by `data.json()` call
      user_data = data;
      fetchMyTweets()
    });

  }

// fetch all tweets
  function fetchMyTweets(){
    console.log(user_data)
    getInfo(`/tweets`, 'GET',  true) 
.then(tweets => {
  console.log(tweets)
  showMyTweets(tweets.tweets);
});
  }

// show user's tweets
  function showMyTweets(tweets) {
    _one("#user-profile").innerHTML = "";
    _one("#tweets").innerHTML = "";
  let oneTweet;
  let tweet_image ='';


    tweets.forEach((tweet) => {
      // if the user id in tweet matches the id of the user who is logged in - display the tweet
      if ( user_data && (tweet.user_id) == user_data.user_info.id) {
console.log(tweet.image)
        if (tweet.image) {
          tweet_image =  `<img class="mt-2 w-full object-cover h-80" src="/images/${tweet.image}">`
        }
      
    oneTweet = `<div class="p-4 border-t border-mediumgrey"  id="${tweet.id}">
      <div class="flex">
      <img class="flex-none w-12 h-12 rounded-full object-cover" src="/images/${tweet.user_id}.jpeg" alt="">
        <div class="w-full pl-4">
          <p class="font-bold">
            ${tweet.user_firstname} ${tweet.user_lastname}
          </p>            
          <p class="font-thin">
            @${tweet.user_name}
          </p>            
          <div class="pt-2 tweet-text">
            ${tweet.text}
          </div>` + tweet_image + 
          `<div class="flex gap-12 w-full mt-4 text-lg">
            
              <i class="fa-solid fa-message ml-auto"></i>
              <i class="fa-solid fa-heart"></i>
              <i class="fa-solid fa-retweet"></i>
              <i class="fa-solid fa-share-nodes"></i>
              <i onclick="delete_tweet('${tweet.id}')" class="fas fa-trash"></i> <i id="edit${tweet.id}" class="fa-solid fa-pen-to-square" onclick="getTweetId(
                event)"></i>
             
          </div>
        </div>
      </div>
    </div>` }

    if (oneTweet) {
      //hide info about no tweets
    _one("#tweets").insertAdjacentHTML("afterbegin", oneTweet)
    if (!_one("#no-tweets-info").classList.contains("hidden")) {
      _one("#no-tweets-info").classList.add("hidden");
    }
    } else if (_one("#no-tweets-info").classList.contains("hidden")) {
      //display info about no tweets
      _one("#no-tweets-info").classList.remove("hidden");
    }
  })

  }
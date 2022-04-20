function _all(q, e=document){return e.querySelectorAll(q)}
function _one(q, e=document){return e.querySelector(q)}


let current_update_tweet_id;


function toggleTweetModal(){
  _one("#tweetModal").classList.toggle("hidden")
}

async function sendTweet(){
  const form = event.target
  // Get the button, set the data-await, and disable it
  const button = _one("button[type='submit']", form)
  console.log(button)
  button.innerText = button.dataset.await
  // button.innerText = button.getAttribute("data-await")
  button.disabled = true
  const connection = await fetch("/api-create-tweet", {
    method : "POST",
    body : new FormData(form)
  })

  const tweet_info = await connection.text() // tweet id will be here
  console.log(tweet_info)
 const tweet_id = tweet_info;



  getInfo('/user-info', 'GET', true)
  .then(data => {
    console.log(data) // JSON data parsed by `data.json()` call
    addTweet(data);
  });


  button.disabled = false
  button.innerText = button.dataset.default

  if( ! connection.ok ){
    return
  }


function addTweet(data) {
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
        </div>
        <div class="flex gap-12 w-full mt-4 text-lg">
            <i onclick="delete_tweet('${tweet_id}', false)" class="fas fa-trash ml-auto"></i>
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

  _one("#tweets").insertAdjacentHTML("afterbegin", tweet)
};

}


async function delete_tweet(tweet_id, isAdmin){
  console.log(tweet_id)
  // Connect to the api and delete it from the "database"
  const connection = await fetch(`/api-delete-tweet/${tweet_id}`, {
    method : "DELETE"
  })
  if( ! connection.ok ){
    alert("uppps... try again")
    return
  }

  console.log(isAdmin)
if (isAdmin) {
  document.querySelector(`#admin-${tweet_id}`).remove()
} else {
  document.querySelector(`[id='${tweet_id}']`).remove()
}
}

function getTweetId(event) {
  const tweet_id = event.target.id.slice(4);
  getInfo('/tweets', 'GET', true)
  .then(data => {
    getCurrentTweetInfo(data, tweet_id) // JSON data parsed by `data.json()` call
  });
_one("#tweetEditModal").classList.toggle("hidden");
}




// Example POST method implementation:
async function getInfo(url, method, isjson) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: method, // *GET, POST, PUT, DELETE, etc.
  });
  console.log(response)
  if (response.status == 200) {
  if  (isjson) {
  return response.json(); // parses JSON response into native JavaScript objects
  } else {
    return response;
  }
} else {
  console.log("Check your connection - status: " + response.status)
}
}


function getCurrentTweetInfo(data, id) {
  data.tweets.map(findTweetText)
  console.log(id)
  current_update_tweet_id = id;


  const tweet_index = data.tweets.findIndex(tweet => tweet.id === id)

  function findTweetText(tweet) {
    console.log(tweet.id)
  }
  _one("#tweet_edit_text").value = data.tweets[tweet_index].text;

  
}

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


function addFollowing(event) {
  const following_id = event.target.id;
  console.log(event.target.innerText)
  if (event.target.innerText == "Follow") {
  getInfo(`/follow-user/${following_id}`, 'POST', false)
  .then(data => {
    console.log(data)
    console.log("hi")
    event.target.innerText = "Following";
}); } else {
  getInfo(`/unfollow-user/${following_id}`, 'DELETE', false)
  .then(data => {
    console.log(data)
    event.target.innerText = "Follow";
});
}
}

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

function showUserTweets(tweets, hideInput) {
  _one("#tweets").innerHTML = "";

  if (hideInput) {_one("#add-tweet").classList.add("hidden")};
  tweets.forEach((tweet) => {
    console.log(tweet)
    let oneTweet = `<div class="p-4 border-t border-mediumgrey">
    <div class="flex">
      <img class="flex-none w-12 h-12 rounded-full object-cover" src="/images/${tweet.user_id}.jpg" alt="">
      <div class="w-full pl-4">
        <p class="font-bold">
          ${tweet.user_first_name} ${tweet.user_last_name}
        </p>            
        <p class="font-thin">
          ${tweet.user_name}
        </p>            
        <div class="pt-2">
          ${tweet.text}
        </div>
        <div class="flex gap-12 w-full mt-4 text-lg">
            <i class="fa-solid fa-message ml-auto"></i>
            <i class="fa-solid fa-heart"></i>
            <i class="fa-solid fa-retweet"></i>
            <i class="fa-solid fa-share-nodes"></i>
            <i class="fa-solid fa-pen-to-square"></i>
        </div>
      </div>
    </div>
  </div>`
  _one("#tweets").insertAdjacentHTML("afterbegin", oneTweet)
  })

} 

function switchMode(event) {
if (event.target.innerText == "Admin") {
  event.target.innerText = "User";
  _one("#admin").classList.remove("hidden");
  _one("#tweets").classList.add("hidden");
} else {
  event.target.innerText = "Admin";
  _one("#admin").classList.add("hidden");
  _one("#tweets").classList.remove("hidden");
}
}

function getTweets() {
console.log()


getInfo(`/tweets`, 'GET',  true) 
.then(tweets => {
  console.log(tweets)
  let searchResults = [];
  searchTweets(tweets, searchResults)
});
}

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

  function hideProfile() {
    _one("#user-profile").innerHTML = "";
    getInfo(`/tweets`, 'GET',  true) 
.then(tweets => {
  showUserTweets(tweets.tweets, false)
  _one("#add-tweet").classList.remove("hidden")
});
  }
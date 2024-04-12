let users = [
  {
    id: 0,
    name: "John",
  },
  {
    id: 1,
    name: "Sam",
  },
  {
    id: 2,
    name: "Mike",
  },
];

let comments = [
  {
    id: 0,
    user_id: 1,
    content: "Hello world!",
  },
  {
    id: 1,
    user_id: 2,
    content: "Hi there",
  },
];

// Fake APIs
function getComments() {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("Received comments successfully");
      resolve(comments);
    }, 2000);
  });
}

function getUsers() {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("Received users successfully");
      resolve(users);
    }, 5000);
  });
}
////

// From clients
// We want to get the users commented
Promise.all([getUsers(), getComments()]).then(([users, comments]) => {
  //   let comment = comments.find((comment) => comment.user_id == 1);
  let result = users.reduce((acc, user) => {
    let comment = comments.find((comment) => user.id == comment.user_id);
    if (comment) acc.push({ name: user.name, comment: comment.content });
    else console.log(`Comment of user ${user.name} not found`);
    return acc;
  }, []);
  let userList = document.querySelector(".user--commented");
  result.forEach((user) => {
    userList.innerHTML += `<li>${user.name}: ${user.comment}</li>`;
  });
});
////

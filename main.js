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
Promise.all([getUsers(), getComments()]).then(([users, comments]) => {
  let ids = comments.map((comment) => comment.user_id);
  let result = users.filter((user) => ids.includes(user.id));
  console.log(result);
});
////

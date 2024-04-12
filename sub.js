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

function getComments() {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("Received comments successfully");
      resolve(comments);
    }, 3000);
  });
}

function getUsersByIds(userIds) {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("Received users successfully");
      resolve(users.filter((user) => userIds.includes(user.id)));
    }, 2000);
  });
}

getComments()
  .then((comments) => {
    let userids = comments.map((comment) => comment.user_id);
    return getUsersByIds(userids);
  })
  .then((usersFiltered) => {
    console.log(usersFiltered);
  });

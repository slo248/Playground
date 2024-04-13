const blogsAPI = "http://localhost:3000/blogs";
const usersAPI = "http://localhost:3000/users";

let currentUserID = 2;

function getUsersFromAPI() {
  return fetch(usersAPI)
    .then((response) => response.json())
    .catch(() => {
      console.log("Error loading users");
    });
}

function getBlogsFromAPI() {
  return fetch(blogsAPI)
    .then((response) => response.json())
    .catch(() => {
      console.log("Error loading blogs");
    });
}

function populateBlogs([users, blogs]) {
  return blogs.map((blog) => {
    let user = users.find((user) => user.id == blog.author_id);
    blog["author"] = user.name;
    return blog;
  });
}

function renderBlogs(blogs) {
  let blogsElement = document.querySelector(".blogs");
  let htmls = blogs.map(
    (blog) => `
        <li>
            <h2>${blog.title}</h2>
            <strong>${blog.author}</strong>
            <p>${blog.content}</p>
        </li>
    `
  );
  let html = htmls.join("");
  blogsElement.innerHTML += html;
}

function start() {
  Promise.all([getUsersFromAPI(), getBlogsFromAPI()])
    .then(populateBlogs)
    .then(renderBlogs);
}

start();

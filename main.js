async function get_data() {
  const url = "http://127.0.0.1:8000/user/";
  const token =
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIxIiwiZW1haWwiOiJ1c2VyMUBnbWFpbC5jb20ifQ.blzIT4skmPFmGMzFjkIpDIaoDIDDon9LZpeMjcFXfxo";

  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      throw new Error("Error");
    }

    const data = await response.json();

    console.log(data);
  } catch (error) {
    console.log(error.message);
  }
}

// get_data()

// const url = "http://127.0.0.1:8000/user/create_user";

function create_user() {
  fetch(url, {
    method: "POST",
    body: JSON.stringify({
      user_id: "carlos",
      user_added: {
        username: "carlos",
        password: "carlos2",
        email: "nicoortega334@gmail.com",
      },
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  }).then((response) => {
    const token_header = response.headers.get("x-token-auth");
    console.log("token: " + token_header);
  });
}

// create_user();

const url_log = "http://127.0.0.1:8000/auth/";

const log = () => {
  fetch(url_log, {
    method: "POST",
    body: JSON.stringify({
      username: "user1",
      password: "password1",
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then((response) => {
      const token_header = response.headers.get("x-token-login");
      if (token_header) {
        console.log("token login \n" + token_header);
        sessionStorage.setItem("jwt_token_log", token_header);
      } else {
        console.error("no token available")
      }
    })
    .catch((error) => {
      console.error("err", error);
    });
};

log()

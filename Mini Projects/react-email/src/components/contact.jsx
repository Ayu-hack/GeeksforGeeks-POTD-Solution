import React, { useRef, useState } from "react";
import emailjs from "@emailjs/browser";
import styled, { createGlobalStyle } from "styled-components";

// npm i @emailjs/browser

const GlobalStyle = createGlobalStyle`
  body {
    background-color: ${(props) => (props.darkMode ? "#0a0a0a" : "#c2bfbf")};
    color: ${(props) => (props.darkMode ? "#cccaca" : "#000")};
  }
`;

const Contact = () => {
  const form = useRef();
  const [darkMode, setDarkMode] = useState(false);

  const sendEmail = (e) => {
    e.preventDefault();

    emailjs
      .sendForm(
        "service_0ipqym9",
        "template_4x1osm5",
        form.current,
        "yPE-wtDAi7vcV5kG3"
      )
      .then(
        (result) => {
          console.log(result.text);
          console.log("message sent");
        },
        (error) => {
          console.log(error.text);
        }
      );
  };

  return (
    <StyledContactForm darkMode={darkMode}>
      <GlobalStyle darkMode={darkMode} />
      <form ref={form} onSubmit={sendEmail}>
        <label>Name</label>
        <input type="text" name="user_name" />
        <label>Email</label>
        <input type="email" name="user_email" />
        <label>Message</label>
        <textarea name="message" />
        <input type="submit" value="Send" />
      </form>
      <ToggleButton onClick={() => setDarkMode(!darkMode)}>
        <Slider darkMode={darkMode} />
      </ToggleButton>
    </StyledContactForm>
  );
};

const StyledContactForm = styled.div`
  width: 400px;

  form {
    display: flex;
    align-items: flex-start;
    flex-direction: column;
    width: 100%;
    font-size: 16px;

    input {
      width: 100%;
      height: 35px;
      padding: 7px;
      outline: none;
      border-radius: 5px;
      border: 1px solid rgb(220, 220, 220);

      &:focus {
        border: 2px solid rgba(0, 206, 158, 1);
      }
    }

    textarea {
      max-width: 100%;
      min-width: 100%;
      width: 100%;
      max-height: 100px;
      min-height: 100px;
      padding: 7px;
      outline: none;
      border-radius: 5px;
      border: 1px solid rgb(220, 220, 220);

      &:focus {
        border: 2px solid rgba(0, 206, 158, 1);
      }
    }

    label {
      margin-top: 1rem;
    }

    input[type="submit"] {
      margin-top: 2rem;
      cursor: pointer;
      background: rgb(249, 105, 14);
      color: white;
      border: none;
    }
  }
`;

const ToggleButton = styled.button`
  position: relative;
  display: inline-block;
  width: 50px;
  height: 25px;
  background-color: #cccaca;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  margin-top: 1rem;
`;

const Slider = styled.div`
  position: absolute;
  top: 0;
  left: ${(props) => (props.darkMode ? "25px" : "0")};
  width: 25px;
  height: 25px;
  border-radius: 50%;
  background-color: #000;
  transition: left 0.3s ease-in-out;
`;

export default Contact;

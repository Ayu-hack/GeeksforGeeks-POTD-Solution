import { TextField } from "@mui/material";
import React from "react";
import "../Styles/Input.css";
import { inputChecks } from "../Utils/inputChecks";

const Input = (props) => {
  return (
    <div className="input-component">
      <p className="input-title">{props.title}</p>
      <TextField
        variant="outlined"
        type={props.type}
        name={props.name}
        {...props.register(props.name, inputChecks(props.type, props.name))}
        multiline={props.multiline}
        rows={5}
        value={props.value}
        onChange={(e) => props.setValue(e.target.value.toString())}
        error={props.error}
        helperText={props.errorMessage ? props.errorMessage : null}
      />
    </div>
  );
};

export default Input;
//RajdeepDey010
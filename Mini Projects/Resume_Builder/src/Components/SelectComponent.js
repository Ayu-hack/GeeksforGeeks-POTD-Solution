import "../Styles/SelectComponent.css";
import React from "react";
import { FormControl, FormHelperText } from "@mui/material";

const SelectComponent = (props) => {
  return (
    <div className="select-component">
      <p className="select-title">{props.title}</p>
      <FormControl fullWidth error={props.error}>
        {props.children}
        <FormHelperText>{props.errorMessage}</FormHelperText>
      </FormControl>
    </div>
  );
};
//RajdeepDey010

export default SelectComponent;
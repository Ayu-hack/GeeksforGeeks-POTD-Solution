import "../Styles/TemplateKeySkill.css";
import { Container } from "@mui/material";
import React from "react";

const TemplateKeySkill = (props) => {
  return (
    <Container>
      <li className="skill">{props.skill}</li>
    </Container>
  );
};

export default TemplateKeySkill;
//RajdeepDey010
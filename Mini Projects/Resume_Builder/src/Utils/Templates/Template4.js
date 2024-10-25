import { Container, Paper } from "@mui/material";
import React from "react";
import "./Template.css";
import HeaderSection from "../../Components/HeaderSection";
import TempHeading from "../../Components/HeadingSection";
import { data } from "../Data/data";
import ExperienceSection from "../../Components/ExperienceSection";
import TemplateEducation from "../../Components/TemplateEducation";
import TemplateKeySkill from "../../Components/TemplateKeySkill";

const Template1 = (props) => {
  const personalinfo = props.personalinfo
    ? props.personalinfo
    : data.personal_info;
  const workexperience = props.workexperience
    ? props.workexperience
    : data.work_experience;
  const educationinfo = props.educationinfo
    ? props.educationinfo
    : data.education_details;
  const skills = props.skills ? props.skills : data.key_skills;

  return (
    <Paper
      sx={{
        width: {
          xs: "350px",
          sm: "400px",
          md: "450px",
          lg: "500px",
          xl: "600px",
        },
        height: {
          xs: "500px",
          sm: "550px",
          md: "600px",
          lg: "650px",
          xl: "700px",
        },
        backgroundColor: "#F8EAE2", // Change background color
        boxShadow: "5px 5px 10px rgba(0, 0, 0, 0.2)", // Add a box shadow
      }}
      id={`${props.index}report`}
      elevation={3}>
      <HeaderSection
        primaryColor={"#333"} // Change primaryColor to a darker color
        secondaryColor={"#333"} // Change secondaryColor to a darker color
        bgColor={"#F8EAE2"} // Change background color to match
        hrcolor={"#333"} // Change horizontal line color
        Hdownheight={"3px"}
        hrsecondcolor={"none"}
        personalInfo={personalinfo}
        workExperience={workexperience}
      />
      <Container>
        <TempHeading color={"#333"} Hupcolor={"#333"} Hupheight={"3px"} Hdowncolor={"none"} Hdownheight={"none"} title={"Professional Experience"} />
        <ul style={{ marginBottom: 10 }}>
          {workexperience.map((experience, index) => {
            return (
              <ExperienceSection
                key={index}
                experience={experience}
              />
            );
          })}
        </ul>
        <TempHeading color={"#333"} Hupcolor={"#333"} Hupheight={"3px"} Hdowncolor={"none"} Hdownheight={"none"} title={"Education"} />
        <TemplateEducation education={educationinfo} />
        <TempHeading color={"#333"} Hupcolor={"#333"} Hupheight={"3px"} Hdowncolor={"none"} Hdownheight={"none"} title={"Key Skills"} />
        <ul style={{ marginBottom: 10 }}>
          {skills.map((skill, index) => {
            return <TemplateKeySkill key={index} skill={skill} />;
          })}
        </ul>
      </Container>
    </Paper>
  );
};

export default Template1;

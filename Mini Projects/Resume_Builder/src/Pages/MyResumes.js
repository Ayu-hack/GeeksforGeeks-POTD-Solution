import "./Styles/MyResumes.css";
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button, Box } from "@mui/material";
import { styled } from "@mui/material/styles";
import Paper from "@mui/material/Paper";
import JsPDF from "jspdf";
import Grid from "@mui/material/Grid";
import SentimentVeryDissatisfiedIcon from "@mui/icons-material/SentimentVeryDissatisfied";
import { connect } from "react-redux";
import { templates } from "../Utils/Data/templates";
import { Navbar, ScreenDarkComponent } from "./";
import {
  addAllExperience,
  addEducation,
  addPersonalInfo,
  editSkill,
  selectResume,
  selectTemplate,
} from "../Redux/Actions/actions";

// details in the local storage are stored in JSON format (key,value) on this page
const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === "dark" ? "#1A2027" : "#fff",
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: "center",
  color: theme.palette.text.secondary,
}));

const StatetoProps = (state) => ({
  selectedTemplateId: state.selectedTemplateReducer.selectedTemplateId,
});

const DispatchtoProps = (dispatch) => ({
  setSelectedTemplateId: (id) => dispatch(selectTemplate(id)),
  setSelectedResumeId: (id) => dispatch(selectResume(id)),
  onAddPersonalInfo: (details) => dispatch(addPersonalInfo(details)),
  setAllExperience: (experiences) => dispatch(addAllExperience(experiences)),
  onAddEducation: (details) => dispatch(addEducation(details)),
  onEditSkill: (skills) => dispatch(editSkill(skills)),
});

const MyResumes = (props) => {
  const [resumes, setResumes] = useState([]);

  useEffect(() => {
    const newResumes = window.localStorage.getItem("resumes")
      ? JSON.parse(window.localStorage.getItem("resumes"))
      : [];

    setResumes(newResumes);
  }, []);

  const navigate = useNavigate();

  const getTemplate = (resume, index) => {
    let template = templates.find(
      (eachTemplate) => eachTemplate.id === resume.template_id
    );
   
    const TemplateComp = React.cloneElement(template.template, {
      personalinfo: resume.personalInfo,
      workexperience: resume.experiences,
      educationinfo: resume.educationInfo,
      skills: resume.skills,
      key: resume.id,
      index: index,
    });

    return TemplateComp;
  };

  const deleteResume = (resume) => {
    let resumes = window.localStorage.getItem("resumes");

    let newResumes = JSON.parse(resumes);
    const newSetOfResumes = newResumes.filter((eachResume) => {
      return eachResume.id !== resume.id;
    });

    window.localStorage.setItem("resumes", JSON.stringify(newSetOfResumes));
    setResumes(newSetOfResumes);
  };

  const downloadResume = (id) => {
    const report = new JsPDF("portrait", "pt", "a4");
    report.html(document.getElementById(`${id}report`)).then(() => {
      report.save(`resume.pdf`);
    });
  };

  const setUserData = (resume) => {

    props.onAddPersonalInfo(resume.personalInfo);


    props.setAllExperience(resume.experiences);


    props.onAddEducation(resume.educationInfo);


    props.onEditSkill(resume.skills);
  };

  const navigateToFillDetails = (resume) => {
    props.setSelectedTemplateId(resume.template_id);
    props.setSelectedResumeId(resume.id);
    setUserData(resume);
    navigate("/template/fill-details");
  };

  return (
    <>
      <Navbar active={"My Resumes"} />
      <div className="my-resumes">
        <Box sx={{ flexGrow: 1 }}>
          <Grid
            container
            justifyContent="center"
            alignItems="center"
            className="grid"
          >
            {resumes.length >= 1 ? (
              resumes.map((resume, index) => {
                return (
                  <Grid
                    item
                    className={`resume `}
                    id={`${index}resume`}
                    margin={2}
                    key={index}
                  >
                    <Item id={`${index}ITEM`}>
                      {getTemplate(resume, index)}
                      <ScreenDarkComponent />
                      <div className="use-template-btn-cont">
                        <Button
                          className="use-template-btn"
                          onClick={() => {
                            downloadResume(index);
                          }}
                          size="medium"
                          variant="contained"
                        >
                          Download
                        </Button>
                        <Button
                          className="use-template-btn"
                          onClick={() => {
                            deleteResume(resume);
                          }}
                          size="medium"
                          variant="contained"
                        >
                          Delete
                        </Button>
                        <Button
                          className="use-template-btn"
                          onClick={() => navigateToFillDetails(resume)}
                          size="medium"
                          variant="contained"
                        >
                          Edit Template
                        </Button>
                      </div>
                    </Item>
                  </Grid>
                );
              })
            ) : (
              <div className="no-resumes-container">
                <SentimentVeryDissatisfiedIcon fontSize="large" />
                <p className="no-resumes-text">
                  You do not have any Resumes yet. Make One to view it here.
                </p>
              </div>
            )}
          </Grid>
        </Box>
      </div>
    </>
  );
};

export default connect(StatetoProps, DispatchtoProps)(MyResumes);
//RajdeepDey010
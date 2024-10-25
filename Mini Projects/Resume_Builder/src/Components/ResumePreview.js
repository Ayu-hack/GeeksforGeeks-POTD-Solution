import "../Styles/ResumePreview.css";
import React, { useState } from "react";
import { Button, CircularProgress, Container, TextField, Box, Modal, Typography } from "@mui/material";
import JsPDF from "jspdf";
import uniqid from "uniqid";
import { connect } from "react-redux";
import { templates } from "../Utils/Data/templates";
import CheckCircleIcon from '@mui/icons-material/CheckCircle';

const mapStatetoProps = (state) => ({
  selectedTemplateId: state.selectedTemplateReducer.selectedTemplateId,
  selectedResumeId: state.selectedTemplateReducer.selectedResumeId,
  personalInfo: state.personalInfoReducer.personalInfo,
  experiences: state.workExperienceReducer.experiences,
  educationInfo: state.educationDetailsReducer.educationInfo,
  skills: state.keySkillsReducer.skills,
});

const mapDispatchtoProps = (dispatch) => ({});
//RajdeepDey010

const ResumePreview = (props) => {
  const [showModal,setShowModal]=useState(false)
  const [loading, setLoading] = useState(false);
  const [resumeName, setResumeName] = useState("");
  const [error, setError] = useState("");

  const getTemplate = (template, index) => {
    // creating a new React element using another element as a starting point.
    if (template.id === props.selectedTemplateId) {
      const TemplateComp = React.cloneElement(template.template, {
        personalinfo: props.personalInfo,
        workexperience: props.experiences,
        educationinfo: props.educationInfo,
        skills: props.skills,
        index: index,
      });
      return TemplateComp;
    }
  };


  const handleSave = () => {
    if (resumeName.length === 0) {
      setError("*Please fill this field");
    } else {
      setError("");
      setLoading(true);
      const report = new JsPDF("portrait", "pt", "a4");
      report
        .html(document.getElementById(`${props.selectedTemplateId - 1}report`))
        .then(() => {
          report.save(`${resumeName}.pdf`);
          setLoading(false);
                    //Saving the user data in localstorage
          let resumes = window.localStorage.getItem("resumes");
          if (resumes) {
            let newResumes = JSON.parse(resumes);

            let resumeFound = newResumes.find(
              (resume) => resume.id === props.selectedResumeId
            );

            if (resumeFound) {
              const allNewResumes = newResumes.map((resume) => {
                if (resume.id === props.selectedResumeId) {
                  return {
                    template_id: props.selectedTemplateId,
                    id: props.selectedResumeId,
                    personalInfo: props.personalInfo,
                    experiences: props.experiences,
                    educationInfo: props.educationInfo,
                    skills: props.skills,
                  };
                } else return resume;
              });

              window.localStorage.setItem(
                "resumes",
                JSON.stringify(allNewResumes)
              );

              window.location.reload();

              return;
            }

            newResumes.push({
              template_id: props.selectedTemplateId,
              id: uniqid(),
              personalInfo: props.personalInfo,
              experiences: props.experiences,
              educationInfo: props.educationInfo,
              skills: props.skills,
            });

            window.localStorage.setItem("resumes", JSON.stringify(newResumes));
          } else {
            window.localStorage.setItem(
              "resumes",
              JSON.stringify([
                {
                  template_id: props.selectedTemplateId,
                  id: uniqid(),
                  personalInfo: props.personalInfo,
                  experiences: props.experiences,
                  educationInfo: props.educationInfo,
                  skills: props.skills,
                },
              ])
            );
          }
          //Redirect user to the myResumes page
          window.location.reload();
        })
        .catch((error) => console.log(error.message));
    }
    setShowModal(true); // Set showPopup state to true after successful download
  };

  const handleBack = () => {
    props.setTab(props.tab - 1);
  };

  return (
    <Container
      sx={{
        padding: {
          xs: "40px 20px",
          md: "60px 80px",
        },
      }}
      className="preview-container">
      <h2 className="preview-header-title">Resume Preview</h2>
      <div className="resume-preview-grid-container">
        <div className="resume-preview-grid-item" id="previewresume">
          {templates.map((template, index) => {
            return getTemplate(template, index);
          })}
        </div>
        <div className="resume-preview-grid-item">
          <div className="resume-save-container">
            <h3 className="resume-save-title">Create File Name</h3>
            <TextField
              value={resumeName}
              onChange={(e) => setResumeName(e.target.value)}
              className="resume-name-field"
              sx={{ width: "70%" }}
              id="outlined-basic"
              variant="outlined"
              error={error.length > 0 ? true : false}
              helperText={error}
            />
            <div className="resume-back-next-container">
              <Button
                onClick={handleBack}
                className="outlined-btn"
                sx={{ marginRight: "20px" }}
                variant="outlined">
                Back
              </Button>
              {loading ? (
                <CircularProgress size={25} />
              ) : (
                <Box>
                <Button
                  onClick={handleSave}
                  className="contained-btn"
                  variant="contained">
                  Save
                </Button>
                {showModal && (
                                <Modal open={showModal}>
                                    <Box sx={{
                                        position: 'absolute',
                                        top: '50%',
                                        left: '50%',
                                        transform: 'translate(-50%, -50%)',
                                        bgcolor: 'background.paper',
                                        boxShadow: 24,
                                        p: 4,
                                        borderRadius: '10px',
                                        maxWidth: '80vw',
                                        maxHeight: '80vh',
                                        overflow: 'auto',
                                        display:'flex',
                                        flexDirection:'column',
                                        alignItems:'center', 
                                        justifyContent:'center',
                                        height:'30%',
                                    }} className={showModal ? 'animate-modal visible' : 'animate-modal'}
                                    >
                                        <CheckCircleIcon color='primary' style={{ fontSize: 80 }} />

                                    <Typography variant='h5'>Your Resume has been Successfully Saved</Typography>
                                    <Box display='flex' flexDirection='column' alignItems='center' justifyContent='center' height='100%'>
                                    </Box>
                                    </Box>
                                </Modal>
                                )}
                </Box>
              )}
            </div>
          </div>
        </div>
      </div>
    </Container>
  );
};

export default connect(mapStatetoProps, mapDispatchtoProps)(ResumePreview);
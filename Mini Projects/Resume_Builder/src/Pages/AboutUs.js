import { Stack, Typography, Box } from "@mui/material";
import LinkedInIcon from "@mui/icons-material/LinkedIn";
import WhatsAppIcon from "@mui/icons-material/WhatsApp";
import FacebookOutlinedIcon from "@mui/icons-material/FacebookOutlined";
import TwitterIcon from "@mui/icons-material/Twitter";
import { GitHub } from "@mui/icons-material";
import Instagram from "@mui/icons-material/Instagram";
import { Link } from "react-router-dom";
import { Navbar } from "./";
import aboutCV from "../Utils/Images/aboutCV.jpg";
// An overview of the website

export default function ButtonMUI() {
  return (
    <>
      <Navbar />
      <Stack p={{ xs: "15px", sm: "25px", md: "40px", lg: "60px " }}>
        <h2 className="template-header-title">Resume-Builder</h2>
        <Stack
          className="midContainer"
          direction={{
            xs: "column-reverse",
            sm: "column-reverse",
            md: "column-reverse",
            lg: "row",
          }}
          spacing={{ xs: 1, sm: 2, md: 4 }}
          mt="20px"
        >
          <Typography
            sx={{
              fontSize: {
                xs: "13px",
                sm: "15px",
                md: "17px",
                lg: "19px",
              },
              paddingRight: {
                xs: "15px",
                sm: "18px",
                lg: "25px",
              },
              textAlign: "justify",
            }}
          >
            Resume Building made easy and efficient.<br/>
         
            ResumeBuilder offers a time-saving solution for crafting professional resumes with ease. With ResumeBuilder, you can effortlessly create a standout resume, potentially increasing your chances of securing your dream job.

Choose from a selection of templates that best suit your needs, add a high-quality profile picture, input your qualifications and work experience, and instantly generate a polished resume. It's as straightforward as that, eliminating the need for extensive time and effort in the resume-building process.

Additionally, access your previously created resumes at any time through the convenient "My Resumes" tab. We wish you success in achieving your aspirations and securing your dream job. Best of luck on your journey!  
          </Typography>
          <Stack
            sx={{
              width: "30%",
              placeSelf: "center",
            }}
          >
            <img
            
              src='https://p2.hiclipart.com/preview/922/970/349/teamwork-icon-job-resume-icon-leader-icon-mobilewash-oman-chamber-of-commerce-and-industry-trade-car-wash-service-gold-png-clipart.png'
              alt="img"
              style={{height:'250px' ,width: '250px'}}
              
            
            />
          </Stack>
        </Stack>
        <Box mt="25px">
          <Typography
            sx={{
              fontSize: {
                xs: "22px",
                sm: "25px",
                md: "27px",
                lg: "30px",
              },
              fontWeight: "400",
              color: "dark",
            }}
          >
            Kindly Share in your circle
          </Typography>
          <Box className="icons">
            <Link to="https://www.instagram.com">
              <Instagram
                sx={{ fontSize: "40px", paddingLeft: "15px" }}
                color="error"
              />
            </Link>

            <Link to="https://www.facebook.com/sarveshkumar.verman">
              <FacebookOutlinedIcon
                sx={{ fontSize: "40px", paddingLeft: "15px" }}
                color="primary"
              />
            </Link>

            <Link to="https://www.linkedin.com/in/sarvesh-kumar-6751391a9/">
              <LinkedInIcon
                sx={{ fontSize: "40px", paddingLeft: "15px" }}
                color="primary"
              />
            </Link>
            <Link to="https://web.whatsapp.com">
              <WhatsAppIcon
                sx={{ fontSize: "40px", paddingLeft: "15px" }}
                color="success"
              />
            </Link>
            <Link to="https://twitter.com/home">
              <TwitterIcon
                sx={{ fontSize: "40px", paddingLeft: "15px" }}
                color="info"
              />
            </Link>
            <Link to="https://github.com/Sarveshkumar0611">
              <GitHub
                sx={{ fontSize: "40px", paddingLeft: "15px", color: "black" }}
              />
            </Link>
          </Box>
        </Box>
      </Stack>
    </>
  );
}

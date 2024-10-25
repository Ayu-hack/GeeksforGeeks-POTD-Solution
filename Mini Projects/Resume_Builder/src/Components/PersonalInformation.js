import "../Styles/PersonalInformation.css";
import { useForm } from "react-hook-form";
import { Avatar, Button, Divider, Paper, Snackbar } from "@mui/material";
import React, { useState, useEffect } from "react";
import { connect } from "react-redux";
import Avatar1 from "react-avatar-edit";
import { styled } from "@mui/material/styles";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import IconButton from "@mui/material/IconButton";
import CloseIcon from "@mui/icons-material/Close";
import { BackNextButton, Input } from "../Pages/index";
import { addPersonalInfo } from "../Redux/Actions/actions";

const mapStateToProps = (state) => ({
  personalInfo: state.personalInfoReducer.personalInfo,
});
//RajdeepDey010

const mapDispatchToProps = (dispatch) => ({
  onAddPersonalInfo: (details) => dispatch(addPersonalInfo(details)),
});

const BootstrapDialog = styled(Dialog)(({ theme }) => ({
  "& .MuiDialogContent-root": {
    padding: theme.spacing(2),
  },
  "& .MuiDialogActions-root": {
    padding: theme.spacing(1),
  },
}));

const PersonalInfoComponent = (props) => {
  const [loading, setLoading] = useState(false);
  const [imgSnackbar, setImgSnackbar] = useState(false);
  const [vertical, setVertical] = useState("bottom");
  const [horizontal, setHorizontal] = useState("center");

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const [img, setImg] = useState(
    props.personalInfo.profileImg.length ? props.personalInfo.profileImg : ""
  );

  const [storeImage, setStoreImage] = useState([]);

  const [open, setOpen] = useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleNext = (data) => {
    if (img.length) {
      setLoading(true);
      props.onAddPersonalInfo({ profileImg: img, ...data });

      setTimeout(() => {
        setLoading(false);
        props.setTab(props.tab + 1);
      }, 1000);
    } else {
      setImgSnackbar(true);
    }
  };

  const BootstrapDialogTitle = (props) => {
    const { children, onClose, ...other } = props;

    return (
      <DialogTitle sx={{ m: 0, p: 2 }} {...other}>
        {children}
        {onClose ? (
          <IconButton
            aria-label="close"
            onClick={onClose}
            sx={{
              position: "absolute",
              right: 8,
              top: 8,
              color: (theme) => theme.palette.grey[500],
            }}
          >
            <CloseIcon />
          </IconButton>
        ) : null}
      </DialogTitle>
    );
  };

  const onCrop = (view) => {
    setImg(view);
  };

  const onClose = (view) => {
    setImg(null);
  };

  const saveImage = () => {
    setStoreImage([{ img }]);
    setOpen(false);
  };

  const handleCloseSnackbar = (event, reason) => {
    if (reason === "clickaway") {
      return;
    }
    setImgSnackbar(false);
  };

  const getWindowSize = () => {
    const { innerWidth, innerHeight } = window;
    return { innerWidth, innerHeight };
  };

  const [windowSize, setWindowSize] = useState(getWindowSize());
  useEffect(() => {
    function handleWindowResize() {
      setWindowSize(getWindowSize());
    }

    window.addEventListener("resize", handleWindowResize);

    return () => {
      window.removeEventListener("resize", handleWindowResize);
    };
  }, []);

  return (
    <Paper className="personal-info-paper" elevation={3}>
      <Avatar
        sx={{
          width: 120,
          height: 120,
          marginBottom: 1,
        }}
        alt="profile img"
        src={
          img.length
            ? img
            : `https://img.icons8.com/color/344/test-account.png`
        }
      />
      <div>
        <Button
          className="change-profile-photo-btn"
          variant="outlined"
          onClick={handleClickOpen}
        >
          Choose profile photo
        </Button>
        <BootstrapDialog
          onClose={handleClose}
          aria-labelledby="customized-dialog-title"
          open={open}
        >
          <BootstrapDialogTitle
            id="customized-dialog-title"
            onClose={handleClose}
          >
            Update Image
          </BootstrapDialogTitle>
          <DialogContent>
            <Avatar1
              width={windowSize.innerWidth > 900 ? 200 : 150}
              height={windowSize.innerHeight > 500 ? 200 : 50}
              onCrop={onCrop}
              onClose={onClose}
            />
          </DialogContent>
          <DialogActions>
            <Button autoFocus variant="contained" onClick={saveImage}>
              Save
            </Button>
          </DialogActions>
        </BootstrapDialog>
      </div>
      <form onSubmit={handleSubmit(handleNext)}>
        <div className="personal-info-form-fields">
          <Input
            title={"First Name"}
            type={"text"}
            name={"firstName"}
            register={register}
            multiline={false}
            value={props.personalInfo.firstName}
            setValue={(value) =>
              props.onAddPersonalInfo({
                ...props.personalInfo,
                firstName: value,
              })
            }
            error={errors.firstName ? true : false}
            errorMessage={errors.firstName ? errors.firstName.message : null}
          />
          <Input
            title={"Last Name"}
            type={"text"}
            name={"lastName"}
            register={register}
            multiline={false}
            value={props.personalInfo.lastName}
            setValue={(value) =>
              props.onAddPersonalInfo({
                ...props.personalInfo,
                lastName: value,
              })
            }
            error={errors.lastName ? true : false}
            errorMessage={errors.lastName ? errors.lastName.message : null}
          />
          <Input
            title={"Email"}
            type={"email"}
            name={"email"}
            register={register}
            multiline={false}
            value={props.personalInfo.email}
            setValue={(value) =>
              props.onAddPersonalInfo({
                ...props.personalInfo,
                email: value,
              })
            }
            error={errors.email ? true : false}
            errorMessage={errors.email ? errors.email.message : null}
          />
          <Input
            title={"Mobile"}
            type={"number"}
            name={"mobile"}
            register={register}
            multiline={false}
            value={props.personalInfo.mobile}
            setValue={(value) =>
              props.onAddPersonalInfo({
                ...props.personalInfo,
                mobile: value,
              })
            }
            error={errors.mobile ? true : false}
            errorMessage={errors.mobile ? errors.mobile.message : null}
          />
        </div>
        <Input
          title={"Address"}
          type={"text"}
          name={"address"}
          register={register}
          multiline={false}
          value={props.personalInfo.address}
          setValue={(value) =>
            props.onAddPersonalInfo({
              ...props.personalInfo,
              address: value,
            })
          }
          error={errors.address ? true : false}
          errorMessage={errors.address ? errors.address.message : null}
        />
        <div style={{ marginTop: 20 }} className="personal-info-form-fields">
          <Input
            title={"City"}
            type={"text"}
            name={"city"}
            register={register}
            multiline={false}
            value={props.personalInfo.city}
            setValue={(value) =>
              props.onAddPersonalInfo({
                ...props.personalInfo,
                city: value,
              })
            }
            error={errors.city ? true : false}
            errorMessage={errors.city ? errors.city.message : null}
          />
          <Input
            title={"Country"}
            type={"text"}
            name={"country"}
            register={register}
            multiline={false}
            value={props.personalInfo.country}
            setValue={(value) =>
              props.onAddPersonalInfo({
                ...props.personalInfo,
                country: value,
              })
            }
            error={errors.country ? true : false}
            errorMessage={errors.country ? errors.country.message : null}
          />
          <Input
            title={"Postal Code"}
            type={"number"}
            name={"postalCode"}
            register={register}
            multiline={false}
            value={props.personalInfo.postalCode}
            setValue={(value) =>
              props.onAddPersonalInfo({
                ...props.personalInfo,
                postalCode: value,
              })
            }
            error={errors.postalCode ? true : false}
            errorMessage={errors.postalCode ? errors.postalCode.message : null}
          />
        </div>
        <Input
          title={"Objective"}
          type={"text"}
          name={"objective"}
          register={register}
          multiline={false}
          value={props.personalInfo.objective}
          setValue={(value) =>
            props.onAddPersonalInfo({
              ...props.personalInfo,
              objective: value,
            })
          }
          error={errors.objective ? true : false}
          errorMessage={errors.objective ? errors.objective.message : null}
        />
        <Divider className="personal-details-divider" />
        <BackNextButton
          loading={loading}
          tab={props.tab}
          nextTitle={"Next"}
          backTitle={"Back"}
        />
      </form>

      <Snackbar
        anchorOrigin={{ vertical, horizontal }}
        key={vertical + horizontal}
        open={imgSnackbar}
        autoHideDuration={1500}
        onClose={handleCloseSnackbar}
        message="Please select a profile image"
      />
    </Paper>
  );
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(PersonalInfoComponent);
//RajdeepDey010
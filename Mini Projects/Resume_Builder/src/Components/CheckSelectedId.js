import React from "react";
import { connect } from "react-redux";
import { Navigate } from "react-router-dom";

const mapStatetoProps = (state) => ({
  selectedTemplateId: state.selectedTemplateReducer.selectedTemplateId,
});

const mapDispatchtoProps = (dispatch) => {
  return {};
};

const CheckSelectedId = (props) => {
  const selectedId = props.selectedTemplateId;
  return selectedId ? props.children : <Navigate to={"/"} />;
};

export default connect(mapStatetoProps, mapDispatchtoProps)(CheckSelectedId);
//RajdeepDey010
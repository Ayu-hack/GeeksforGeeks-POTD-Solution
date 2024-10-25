import React from "react";
import "../Styles/HeadingSection.css";

const TempHeading = (props) => {
  return (
    <div>
      <hr style={{ backgroundColor: props.Hupcolor, height: props.Hupheight }} className="vertical-line" />
      <h2
        style={{ color: props.color }}
        className="professional-experience-heading">
        {props.title}
      </h2>
      <hr style={{ backgroundColor: props.Hdowncolor, height: props.Hdownheight }} className="vertical-line" />
    </div>
  );
};

export default TempHeading;
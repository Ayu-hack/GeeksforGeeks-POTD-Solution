
const initialSelectedTemplateState = {
  selectedTemplateId: null,
  selectedResumeId: null,
};

const initialPersonalInfoState = {
  personalInfo: {
    profileImg: "",
    firstName: "",
    lastName: "",
    email: "",
    mobile: "",
    address: "",
    city: "",
    country: "",
    postalCode: "",
    objective: "",
  },
};

const initialWorkExperienceState = {
  experiences: [
    {
      id: 1,
      jobTitle: "",
      organizationName: "",
      startYear: "",
      endYear: "",
    },
  ],
};

const initialEducationState = {
  educationInfo: {
    domain: "",
    university: "",
    degree: "",
    startYear: "",
    endYear: "",
  },
};

const initialSkillsState = {
  skills: ["", "", ""],
};


export const selectedTemplateReducer = (
  state = initialSelectedTemplateState,
  action
) => {
  switch (action.type) {
    case "SELECTTEMPLATE":
      return { ...state, selectedTemplateId: action.payload };
    case "SELECTRESUME":
      return { ...state, selectedResumeId: action.payload };
    default:
      return state;
  }
};

export const personalInfoReducer = (
  state = initialPersonalInfoState,
  action
) => {
  switch (action.type) {
    case "ADDPERSONALINFO":
      return {
        ...state,
        personalInfo: { ...state.personalInfo, ...action.payload },
      };
    default:
      return state;
  }
};

export const workExperienceReducer = (
  state = initialWorkExperienceState,
  action
) => {
  switch (action.type) {
    case "ADDEXPERIENCE":
      return {
        ...state,
        experiences: [...state.experiences, action.payload],
      };
    case "ADDALLEXPERIENCE":
      return {
        ...state,
        experiences: action.payload,
      };
    default:
      return state;
  }
};

export const keySkillsReducer = (state = initialSkillsState, action) => {
  switch (action.type) {
    case "ADDNEWSKILLS":
      return { ...state, skills: [...state.skills, ""] };
    case "EDITSKILL": {
      return {
        ...state,
        skills: action.payload,
      };
    }
    case "DELETESKILL": {
      const newSkills = state.skills.filter(
        (skill, id) => id !== action.payload
      );

      return { ...state, skills: newSkills };
    }
    default:
      return state;
  }
};

export const educationDetailsReducer = (
  state = initialEducationState,
  action
) => {
  switch (action.type) {
    case "ADDEDUCATION":
      return { ...state, educationInfo: action.payload };
    default:
      return state;
  }
};
export const inputChecks = (type, name) => {
  if (type === "text") {
    return { required: "*Please fill this field" };
  } else if (type === "email") {
    return {
      required: "*Please fill this field",
      pattern:
        /^[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*$/,
    };
  } else if (type === "number") {
    switch (name) {
      case "mobile":
        return {
          required: "*Please fill this field",
          minLength: { value: 10, message: "*Invalid mobile number " },
          maxLength: { value: 12, message: "*Invalid mobile number" },
        };
      case "postalCode":
        return {
          required: "*Please fill this field",
          minLength: { value: 6, message: "*Invalid postal code" },
          maxLength: { value: 6, message: "*Invalid postal code" },
        };
      default:
        return { required: "*Please fill this field" };
    }
  }
};

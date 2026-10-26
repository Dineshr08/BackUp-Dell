export const createUserValidation = {
  userName: {
    notEmpty: {
      errorMessage: "username must not be empty",
    },
    isLength: {
      options: {
        min: 3,
        max: 12,
      },
      errorMessage: "user name length must be between 3 to 12 character length",
    },
    isString: {
      errorMessage: "user name must be string",
    },
    age: {
      notEmpty: {
        errorMessage: "username must not be empty",
      },
    },
  },
};

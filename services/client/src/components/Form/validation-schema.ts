import * as yup from 'yup';

export enum FormInputType {
  text = 'text',
  email = 'email',
  password = 'password'
}

export interface FormInput {
  type: FormInputType;
  name: string;
}

export function createFormSchema(formInputs: FormInput[]) {
  return yup.object().shape(mapInputsToSchema(formInputs));
}

export function mapInputsToSchema(shape: FormInput[] = []) {
  const formInputs = {};

  shape.forEach((input: any) => {
    formInputs[input.name] = mapInputToSchema(input);
  });

  return formInputs;
}

export function mapInputToSchema({ type }: FormInput) {
  switch (type) {
    case 'email':
      return yup
        .string()
        .trim()
        .email('Please enter a valid email')
        .required('Email is required');
    case 'password':
      return yup.string().required();
    case 'text':
      return yup
        .string()
        .trim()
        .required();
    default:
      return yup.string();
  }
}

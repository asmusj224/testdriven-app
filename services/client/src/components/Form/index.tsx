import React from 'react';
import { Formik, Field } from 'formik';
import { createFormSchema, FormInput } from './validation-schema';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';

interface FormProps {
  initialValues: Object;
  inputs: FormInput[];
  handleSubmit: (values: any) => void;
}

export default ({ initialValues, inputs, handleSubmit }: FormProps) => (
  <div>
    <Formik
      initialValues={initialValues}
      enableReinitialize={true}
      validationSchema={() => createFormSchema(inputs)}
      onSubmit={(values, actions) => {
        actions.resetForm();
        handleSubmit(values);
      }}
      render={props => {
        return (
          <form onSubmit={props.handleSubmit}>
            {inputs.map((input: FormInput, index: number) => (
              <div key={index}>
                <Field
                  type={input.type}
                  name={input.name}
                  // TODO add support for additional form fields
                  render={({ field, form }) => (
                    <TextField
                      label={field.name}
                      fullWidth
                      name={field.name}
                      value={field.value}
                      type={input.type}
                      error={Boolean(
                        form.errors[input.name] && form.touched[input.name]
                      )}
                      onChange={form.handleChange}
                      onBlur={form.handleBlur}
                      helperText={
                        form.errors[input.name] &&
                        form.touched[input.name] &&
                        String(form.errors[input.name])
                      }
                    />
                  )}
                />
              </div>
            ))}
            <Button
              style={{ marginTop: '2rem' }}
              variant="contained"
              color="primary"
              type="submit"
              fullWidth
            >
              Submit
            </Button>
          </form>
        );
      }}
    />
  </div>
);

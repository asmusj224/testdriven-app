import React from 'react';
import config from 'next/config';
import Form from '../Form';
import { FormInputType } from '../Form/validation-schema';

const {
  publicRuntimeConfig: { REACT_APP_USERS_SERVICE_URL }
} = config() || {
  publicRuntimeConfig: { REACT_APP_USERS_SERVICE_URL: 'http://localhost:5001' }
};

export default () => (
  <div>
    <Form
      handleSubmit={({ email, password }) =>
      }
      initialValues={{ email: '', password: '' }}
      inputs={[
        { type: FormInputType.email, name: 'email' },
        { type: FormInputType.password, name: 'password' }
      ]}
    />
  </div>
);

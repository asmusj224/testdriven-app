import * as React from 'react';
import { NextPage } from 'next';
import CreateUser from '../src/components/CreateUser';

const IndexPage: NextPage = () => (
  <div>
    <CreateUser />
  </div>
);

export default IndexPage;

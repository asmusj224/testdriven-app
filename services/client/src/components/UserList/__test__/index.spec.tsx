import React from 'react';
import { shallow } from 'enzyme';

import UsersList from '../';

const users = [
  {
    active: true,
    email: 'test@test.com',
    id: '1'
  }
];

test('UsersList renders properly', () => {
  const wrapper = shallow(<UsersList users={users} />);
  const element = wrapper.find('h4');
  expect(element.length).toBe(1);
  expect(element.get(0).props.children).toBe('test@test.com');
});

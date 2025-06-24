import { render, screen, waitFor } from '@testing-library/react';
import App from './App';

beforeAll(() => {
  global.fetch = jest.fn(() =>
    Promise.resolve({ json: () => Promise.resolve({ message: 'Hello, World!' }) })
  );
});

afterAll(() => {
  global.fetch.mockClear();
  delete global.fetch;
});

test('renders FastAPI + React Hello World and fetches message', async () => {
  render(<App />);
  expect(screen.getByText(/FastAPI \+ React Hello World/i)).toBeInTheDocument();
  await waitFor(() => expect(screen.getByText('Hello, World!')).toBeInTheDocument());
});

export default {
  extends: ['@commitlint/config-conventional'],
  rules: {
    // Allow dependabot commits
    'subject-empty': [0, 'never'],
    'type-empty': [0, 'never'],
    // Custom rule for dependabot
    'header-max-length': [2, 'always', 100],
  },
  ignores: [
    // Ignore dependabot commits
    (message) => message.includes('dependabot'),
    (message) => message.includes('Signed-off-by: dependabot[bot]'),
    // Ignore merge commits
    (message) => message.startsWith('Merge '),
  ],
};

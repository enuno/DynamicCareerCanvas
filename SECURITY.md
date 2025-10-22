# Security Policy

## Reporting Security Issues

If you discover a security vulnerability, please email **enuno@proton.me** directly rather than opening a public issue.

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if you have one)

I'll respond within 48-72 hours.

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest (main branch) | ✓ |
| Older versions | ✗ |

## Security Practices

This is a static Jekyll site with minimal attack surface, but we still:

- Keep dependencies updated (Dependabot enabled)
- Scan for vulnerabilities in CI/CD
- Never commit secrets or API keys
- Use HTTPS for all external resources
- Review all contributions

## What to Avoid

**Don't commit:**
- API keys or tokens
- Passwords or credentials
- Private keys
- `.env` files with secrets
- Personal information

**If you accidentally commit a secret:**
1. Rotate/revoke it immediately
2. Remove it from git history
3. Notify the project owner

## GitHub Security Features

This repo uses:
- Dependabot alerts
- Security scanning
- Secret scanning
- Branch protection

## Third-Party Dependencies

Dependencies are managed via:
- Bundler (Ruby gems) - `Gemfile.lock`
- Jekyll plugins - listed in `_config.yml`

Run `bundle audit` to check for known vulnerabilities.

## Questions?

Security questions? Email enuno@proton.me

---

**Last Updated**: 2025-10-21

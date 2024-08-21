# 🚀 Dynamic Resume Builder

Welcome to my **Dynamic Resume Builder**! This project leverages the power of **GitHub**, **GitHub Actions**, **Jekyll**, and **GitHub Pages** to automatically generate and host my resume. With each update to my resume source file, the system automatically rebuilds and redeploys the site—keeping my resume fresh and always up-to-date.

## 🌟 Features

- **Automated Deployment:** No more manual uploads or deployments. Every change you make is automatically reflected on the live site.
- **Markdown Simplicity:** Edit your resume using Markdown—a simple and easy-to-read format.
- **Always Live:** Hosted on GitHub Pages, ensuring your resume is always accessible online.
- **Version Control:** Track your career progress over time with Git's version history.

## 🛠️ Technology Stack

- **[Jekyll](https://jekyllrb.com/):** Static site generator that converts Markdown into a beautiful, responsive HTML resume.
- **[GitHub Actions](https://github.com/features/actions):** Automates the build and deployment process, triggered on every push to the main branch.
- **[GitHub Pages](https://pages.github.com/):** Hosts the generated site, making it accessible at `https://yourusername.github.io/resume/`.
- **[Modern-Resume-Theme](https://github.com/sproogen/modern-resume-theme):** A modern simple static resume template and theme.

## 📂 Project Structure

Here's a quick overview of the key files and directories in this repository:

- `resume.md`: The source file for my resume, written in Markdown.
- `_config.yml`: Jekyll configuration file—customizes the site’s title, theme, and more.
- `_layouts/default.html`: The HTML template that structures the resume content.
- `.github/workflows/jekyll.yml`: GitHub Actions workflow that automates the build and deploy process.

## 🚀 Getting Started

If you'd like to set up a similar system for your own resume, follow these steps:

1. **Fork this repository** to your own GitHub account.
2. **Customize the `resume.md` file** with your own information.
3. **Push your changes**—GitHub Actions will automatically rebuild and deploy your resume.
4. **Check out your live resume** at `https://yourusername.github.io/resume/`.

## 🤖 How It Works

1. **Edit**: Make changes to the `resume.md` file.
2. **Push**: Push the changes to the `main` branch.
3. **Automate**: GitHub Actions kicks in, building the Jekyll site and deploying it to GitHub Pages.
4. **View**: Your updated resume is live and accessible online!

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to explore, fork, and customize this project to suit your own needs. If you have any questions or suggestions, don't hesitate to open an issue or reach out!

Happy coding! ✨
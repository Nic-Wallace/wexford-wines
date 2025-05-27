# [wexford-wines](https://wexford-wines-e7893e8780a4.herokuapp.com)

Developer: Nick Wallace ([Nic-Wallace](https://www.github.com/Nic-Wallace))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Nic-Wallace/wexford-wines)](https://www.github.com/Nic-Wallace/wexford-wines/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Nic-Wallace/wexford-wines)](https://www.github.com/Nic-Wallace/wexford-wines/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Nic-Wallace/wexford-wines)](https://www.github.com/Nic-Wallace/wexford-wines)


![screenshot](documentation/mockup.png)

Wexford Wines is a mock site for the proposed business of the same name based in Wexford, Ireland. The site is streamlined, easy to use and easy on the eyes, as the business appeals to appreciators of high-end wines that are sleek and sophisticated. This site gives the business an extra edge, being able to expand their market and reach more customers online with a fashionable and user-friendly website.

source: [wexford-wines amiresponsive](https://ui.dev/amiresponsive?url=https://wexford-wines-e7893e8780a4.herokuapp.com)

> [!IMPORTANT]
> The examples in these templates are strongly influenced by the Code Institute walkthrough project called "Boutique Ado".

## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**
- Provide a sleek and sophisticated site to sell high-end wines.
- Give customers a pleasant and stress-free experience of using the site and making a purchase with ease.
- Enable site owners to efficiently create and manage listings on the store.

**Primary User Needs**
- Guest users need to view and purchase items easily, with the option of creating an account or contacting the business.
- Customers with an account need to be able to manage their account details and view their order history.
- Site owners need to be abble to manage their site content efficiently.

**Business Goals**
- Improve sales be reaching a larger customer base and provide them with a positive user experience to encourage purchase.
- Gain loyal customers by encouraging account creation and interaction with the business via newsletter and contact form.
- Manage the site inventory to keep it up to date.

#### 2. Scope

**[Features](#features)** (see below)

**Content Requirements**
- Wine listing with image, wine name, taste profile, country of origin, wine colour and price.
- A responsive site that gives clear prompts for user actions and confirms these actions.
- Contact form and newsletter sign up.
- Email confirmations, order history, useful redirection.
- FAQ page with useful questions and answers.
- Secure payment processing using Stripe.
- Link to map of location of the business.
- 404 page to notify users that the page they are looking for doesn't exist.

#### 3. Structure

**Information Architecture**
- **Navigation Menu**:
  - Links to Home, All Wines, Colour filter, Country filter, Contact,Newsletter, FAQ, and Account area.
- **Hierarchy**:
  - Clear wine filters for easy navigation.
  - Cart and checkout options clearly displayed to prompt purchase.

**User Flow**
1. Guest user visits the store → filters wine by colour or country.
2. Guest user adds wines to cart → proceeds to checkout.
3. Guest user creates an account or logs in during checkout → completes purchase.
4. Guest user navigates to contact page → fills in form to message the business.
5. Guest user seeks an answer to a question → seeks and finds relevant information on FAQ page.
6. Guest user navigates to newsletter page → signs up and recieves email confirmation.
7. Guest user visits contact page → clicks external link to view location of business.
8. Returning customer logs in → views their order history.
9. Returning customer logs in → can update their delivery details.
10. Site owners manage inventory → add, update, or delete wine listings.

#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)

### Colour Scheme

I used [coolors.co](https://coolors.co/080708-3772ff-df2935-fdca40-e6e8e6) to generate my color palette.

- `#585858` primary text.
- `#FFFFFF` primary highlights.
- `#000000` secondary text.
- `#7F2A40` secondary highlights.

![screenshot](documentation/coolors.png)

### Typography

- [Lora](https://fonts.google.com/specimen/Lora) was used for all site text for coherence, the site header was styled for a more eye-catching title.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the icons in the navigation bar.
- [Favicon.io](https://favicon.io) was used to find the favicon for the site.

## Wireframes

Following best practice, I developed wireframes for desktop, tablet and mobile. I sketched the wireframes so I took pictures of these.

| Page | Desktop, Tablet, Mobile |
| --- | --- |
| Register | ![screenshot](documentation/wireframes/register.jpg) |
| Login | ![screenshot](documentation/wireframes/login.jpg) |
| Profile | ![screenshot](documentation/wireframes/profile.jpg) |
| Homepage | ![screenshot](documentation/wireframes/homepage.jpg) |
| Wines | ![screenshot](documentation/wireframes/wines.jpg) |
| Wine Details | ![screenshot](documentation/wireframes/wine-details.jpg) |
| Cart | ![screenshot](documentation/wireframes/cart.jpg) |
| Checkout | ![screenshot](documentation/wireframes/checkout.jpg) |
| Checkout Success | ![screenshot](documentation/wireframes/checkout-success.jpg) |
| Add listing | ![screenshot](documentation/wireframes/add-listing.jpg) |
| Edit listing | ![screenshot](documentation/wireframes/edit-listing.jpg) |
| Newsletter | ![screenshot](documentation/wireframes/newsletter.jpg) |
| Contact | ![screenshot](documentation/wireframes/contact.jpg) |
| 404 | ![screenshot](documentation/wireframes/404.jpg) |
| FAQ | ![screenshot](documentation/wireframes/faq.jpg) |

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a site admin | I can add new wines | so that I can keep the site up to date with new products |
| As a site admin | I can view and edit wine listings | so that I can keep the site up to date |
| As a site admin | I can delete wine listings | so that I can keep the site up to date with what is available to buy |
| As a site admin | I can log in and complete authentication | so that I can access the admin tools and keep the site secure |
| As a site user | I can view and add products to cart | so that I can view and later purchase products in one go |
| As a site user | I can modify products in my cart | so that I can remove an item or update the amount of each item I want |
| As a site user | I can be informed of any actions I make | so that I know if my action was successful, which could not be completed and why |
| As a site user | I can view a product and its relevant information | so that I can find out more about the product |
| As a site user | I can view a list of all wines | so that I can know my options and select one to view |
| As a site user | I can login to the site | so that I can have my order history collected in one place to review |
| As a site user | I can login, logout, and delete my account | so that I can have control over my account |
| As a site user | I can sign up to a newsletter | so that I can be kept up to date with new wine products and events |
| As a site user | I can view an FAQ page | so that I can get fast answers to any questions I may have |
| As a site user | I can find and fill out a contact form with a message | so that I can communicate with the business |

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png) |
| Wine List | Users can browse all available wines with sorting, filtering by colour or country, and search functionality. | ![screenshot](documentation/features/wine-list.png) |
| Listing Details | Displays detailed information about a selected wine listing, including its image, name, country of origin, colour, taste profile, and price. | ![screenshot](documentation/features/listing-details.png) |
| Add to Cart | Users can add items to their shopping cart, with mini view of their cart in a notification to confirm and prompt checkout. | ![screenshot](documentation/features/add-to-cart.png) |
| View Cart | Users can view the contents of their shopping cart, adjust quantities, or remove items. | ![screenshot](documentation/features/view-cart.png) |
| Checkout | Users can proceed to checkout, where they provide their delivery details and payment information using Stripe. | ![screenshot](documentation/features/checkout.png) |
| Order Confirmation | Users receive an on-screen and email confirmation with details of their purchase. | ![screenshot](documentation/features/order-confirmation.png) |
| Profile Management | Users can manage their profile information, including their default delivery address and order history. | ![screenshot](documentation/features/profile-management.png) |
| Order History | Users can view their previous orders and view details of each order, including order number, date, items and order total. | ![screenshot](documentation/features/order-history.png) |
| Listing Management | Superusers can add, edit, and delete products from the site via a CRUD interface. | ![screenshot](documentation/features/listing-management.png) |
| Newsletter | Users can register their email address to receive newsletters from the site. Currently, this only stores the email in the database. | ![screenshot](documentation/features/newsletter.png) |
| Contact | Users can submit a message via the contact form, which stores their name, email, and message in the database. They can also find the location of the store here. | ![screenshot](documentation/features/contact.png) |
| FAQs | Admins can manage frequently asked questions, which are displayed on the site for users. | ![screenshot](documentation/features/faqs.png) |
| User Feedback | Clear and concise Django messages are used to provide feedback to users when interacting with various features (e.g., adding products to the cart, checking out, etc.). | ![screenshot](documentation/features/user-feedback.png) |
| Heroku Deployment | The site is deployed to Heroku, making it accessible online for users. | ![screenshot](documentation/features/heroku.png) |
| SEO | SEO optimization with a sitemap.xml, robots.txt, and appropriate meta tags to improve search engine visibility. | ![screenshot](documentation/features/seo.png) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |

### Future Features

- **All Wines page pagination**: View a select amount of listings per page and include arrows to next and previous pages for a better browsing experience.
- **Reviews & Ratings**: Add functionality for users to leave reviews for wines, including a star rating.
- **Saved cart for registered users**: Automatically save the shopping cart of a logged in user so that they can view it when they log in on any device.
- **Multi-Currency and Multi-Language Support**: Expand the application to support multiple currencies and languages to increase customer base.
- **Delivery calculation**: Add delivery cost and automatically calculate it based on the country of the user at checkout.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Jest-grey?logo=jest&logoColor=c21325)](https://jestjs.io) | Automated JavaScript testing. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) | Online secure payments of e-commerce products/services. |
| [![badge](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) | Sending emails in my application. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |

## Database Design

### Data Model

Entity Relationship Diagrams (ERD) helped me visualize the database architecture before creating the models. Understanding the relationships between different tables helped me save time later in the project.

![screenshot](documentation/erd.png)

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
---
config:
theme: forest
---
erDiagram
    User ||--|| UserProfile : has
    UserProfile ||--o{ Order : places
    Order ||--o{ OrderLineItem : contains
    OrderLineItem ||--|| Listing : includes
    Listing }o--|| Colour : has
    Listing }o--|| Country : from

    UserProfile {
        int user_id FK
        string default_phone_number
        string default_street_address1
        string default_street_address2
        string default_county
        string default_country
        string default_postcode
    }

    Order {
        string order_number
        int user_profile_id FK
        string full_name
        string email
        string phone_number
        string street_address1
        string street_address2
        string county
        string postcode
        string country
        datetime date
        decimal order_total
        decimal grand_total
    }

    OrderLineItem {
        int order_id FK
        int wine_id FK
        int quantity
        decimal lineitem_total
    }

    Listing {
        string name
        int wine_colour_id FK
        int country_id FK
        string taste_profile
        string image
        decimal price
        boolean is_public
    }

    Colour {
        string name
    }

    Country {
        string name
    }

    Contact {
        string email
        string name
        text message
        datetime sent
    }

    FAQ {
        string question
        text answer
    }

    Newsletter {
        string email
    }
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqNVduO2jAQ_ZXIzywKWQhL3latVqq66kVVXyokZJIBrDp21h6LpcC_d3JjQy7s-sk5czyXM2PnyGKdAIsYmM-Cbw1Pl8qj9duC8U6nu7vTqdj_MHojJHiRt-P2jVLDOVMfve8moWORl0keQ0UrsSbhWSj4gpASMdYKuVBN6sVaRX8WFoXaElmoWLqk9lvjZ13QPmmpnWnm1yE4heZAjI3RVGW3iGMJ5Uso9ByZViLxnr6-4RZN7jKBDXcSV9lOK1gpl67BDJLoEwBXPEkMWDv5IC8Y5MV5IYfbZjNsz7TFvOcl4VwLUbbp2Dmmc7xT4kWfrNRuQKeNk3KleAodC6RcyA56U8_3dHxPvwHdrvVo85tCJhwBRQrFpgFDLFIuK6VQI5ddI90slTSN18Jfhr41g6XPlri5YU8H-vAXxxWKZpl1BpJOCArRm0R9V7r9v-7eJXRcXLe-DCrZBiYCuUWop6ZjpUS3PcpmRsQNeK21BK48YVeZW0sRt4qpnoJbtTS45avwQTK9VjH2kPvH-Vo7hFf0UhrN6xrrobKgsBXv6fFnT6wXB9QsrVqeubL7-tZcPHyDvZWA2Hu1G0nTATZiKRiCEvobFOQlwx1QBSyibcLN3yVbqjPxuEP966BiFqFxMGIuy6uo_h8s2nBpCc24YtGRvbJoOnkY-_e-P11M_HkYziYjdiA0HIfBdDGfLR78RTC798PziP3Tmjz444f5zKcVhP587gezwtufwlaGNNptd5dQW5NnXVlA0Z0p-sqiYHH-D9beK_w)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/Nic-Wallace/wexford-wines/projects) served as an Agile tool for this project. Through it, EPICs, User Stories and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)
![screenshot](documentation/gh-projects-user-story.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/Nic-Wallace/wexford-wines/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues/Nic-Wallace/wexford-wines)](https://www.github.com/Nic-Wallace/wexford-wines/issues) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/Nic-Wallace/wexford-wines)](https://www.github.com/Nic-Wallace/wexford-wines/issues?q=is%3Aissue+is%3Aclosed) | ![screenshot](documentation/gh-issues-closed.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Ecommerce Business Model

Wexford Wines is a simple **Business to Customer**, or **B2C** website. This is because it is focused solely on selling products to the customer in one purchase, instead of subscription for example.

This site is in early stages of development, and while it has functionality for its purpose, it already has order history for logged in customers, a newsletter sign up, a contact form, and a frequently asked questions section.

The business can soon use the newsletter list to build positive customer relationships by offering them exclusives, discounts, and much more.

Wexford Wines can also use their social media platforms to generate a community of customers and encourage others to join and become loyal customers over time. They curently have a Facebook page (see below).

## SEO & Marketing

### Keywords

I made a list of keywords that are appropriate to my site and will help connect the business with customers who are more likely to be interested in the site and make a purchase after using these keywords in a search engine to find the site. There are two types of keywords included:

- Short-tail keywords
- Long-tail keywords

### Sitemap

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) to generate a sitemap.xml file. This was generated using my deployed site URL: https://wexford-wines-e7893e8780a4.herokuapp.com

After it finished crawling the entire site, it created a [sitemap.xml](sitemap.xml), which I've downloaded and included in the repository.

### Robots

I've created the [robots.txt](robots.txt) file at the root-level. Inside, I've included the default settings:

```txt
User-agent: *
Disallow:
Sitemap: https://wexford-wines-e7893e8780a4.herokuapp.com/sitemap.xml
```

Further links for future implementation:
- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)

### Social Media Marketing

Using social media sites with a large user base like Facebook, can help create an interactive user base and reach, which in turn increases sales.

I've created a mockup Facebook business account using the [Balsamiq template](https://code-institute-org.github.io/5P-Assessments-Handbook/files/Facebook_Mockups.zip) provided by Code Institute.

![screenshot](documentation/mockup-facebook.png)

### Newsletter Marketing

I added a newsletter sign-up form on my site, to allow users to sign up with their email address to be included in the newsletter send out list which will include discounts, exclusives and more. I outline how I did this below: 

**Custom Django Model Newsletter**

- Create a custom `newsletter` app in your project, with a custom model/class called `Newsletter`.
- This method satisfies two assessment criteria:
    1. include a newsletter
    2. one of your 3 required custom models
- It doesn't need anything except the `email` field on the model, but feel free to add more if you need.
- Example:

    ```python
    class Newsletter(models.Model):
    """
    newsletter model
    """
    email = models.EmailField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.email
    ```

## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://wexford-wines-e7893e8780a4.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user-inserts-own-gmail-api-key |
| `EMAIL_HOST_USER` | user-inserts-own-gmail-email-address |
| `SECRET_KEY` | any-random-secret-key |
| `STRIPE_PUBLIC_KEY` | user-inserts-own-stripe-public-key |
| `STRIPE_SECRET_KEY` | user-inserts-own-stripe-secret-key |
| `STRIPE_WH_SECRET` | user-inserts-own-stripe-webhook-secret |
| `DEFAULT_FROM_EMAIL` | user-inserts-own-default-email |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
    - `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
    - `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
    - `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
    - `https://wexford-wines-e7893e8780a4.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
    - `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (*verify your password and account*)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords** (*search for it at the top, if not*).
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
    - Any custom name, such as "Django" or `wexford-wines`
- You'll be provided with a 16-character password (API key).
    - Save this somewhere locally, as you cannot access this key again later!
    - If your 16-character password contains *spaces*, make sure to remove them entirely.
    - `EMAIL_HOST_PASS` = user's 16-character API key
    - `EMAIL_HOST_USER` = user's own personal Gmail email address

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ["SECRET_KEY"] = "any-random-secret-key"
os.environ["DATABASE_URL"] = "user-inserts-own-postgres-database-url"
os.environ["CLOUDINARY_URL"] = "user-inserts-own-cloudinary-database-url"
os.environ["STRIPE_PUBLIC_KEY"] = "user-inserts-own-stripe-public-key"
os.environ["STRIPE_SECRET_KEY"] = "user-inserts-own-stripe-secret-key"
os.environ["EMAIL_HOST_PASS"] = "user-inserts-own-gmail-host-api-key"
os.environ["EMAIL_HOST_USER"] = "user-inserts-own-gmail-email-address"
os.environ["DEFAULT_FROM_EMAIL"] = "user-inserts-own-gmail-email-address"

# local environment only (do not include these in production/deployment!)
os.environ["DEVELOPMENT"] = "1"
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/Nic-Wallace/wexford-wines).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
    - `git clone https://www.github.com/Nic-Wallace/wexford-wines.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/Nic-Wallace/wexford-wines)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/Nic-Wallace/wexford-wines).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Boutique Ado](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Stripe](https://docs.stripe.com/payments/elements) | Online payment services |
| [Gmail API](https://developers.google.com/gmail/api/guides) | Sending payment confirmation emails |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |
| [Mini Webtool](https://miniwebtool.com/django-secret-key-generator/) | Generate Django secret key |

### Media

| Source | Notes |
| --- | --- |
| [Flaticon](https://www.flaticon.com/free-icon/grape_4698346?term=grape&page=1&position=73&origin=search&related_id=4698346) | Generating the favicon (iconixar) and image placeholder (Icon.doit) |
| [Mitchell & Son](https://mitchellandson.com) | Images for the wine listings |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [Freepik](https://www.freepik.com/free-photo/top-view-organinc-grapes-wine_6595541.htm#fromView=search&page=2&position=1&uuid=86e7f38a-5e1f-468a-b5d4-db911b3febb9&query=Wine) | Background wallpaper |
| [TinyPNG](https://tinypng.com) | Compressing images < 5MB |
| [Cloud Convert](https://cloudconvert.com/webp-to-png) | Converting images from WebP to PNG |

### Acknowledgements

- I would like to give a huge thank you to my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for all of his support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
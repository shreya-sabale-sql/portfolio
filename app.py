import streamlit as st
import streamlit.components.v1 as components

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Shreya Sabale | Data Analyst",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------
# CSS
# -------------------------------------------------
st.markdown("""
<style>
body { background-color: #ffffff; }

.section-title {
    font-size: 30px;
    font-weight: 600;
    margin-top: 40px;
}

.card {
    background: #f9f9f9;
    border-radius: 14px;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.08);
    padding: 16px;
    margin-bottom: 25px;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 10px 28px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# STATE
# -------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# -------------------------------------------------
# TOP BAR
# -------------------------------------------------
colA, colB = st.columns([6, 1])
with colB:
    st.download_button(
        "📄 Resume",
        open("assets/resume.pdf", "rb"),
        "Shreya_Sabale_Resume.pdf"
    )

# -------------------------------------------------
# HOME
# -------------------------------------------------

if st.session_state.page == "Home":

    left, right = st.columns([1,2])

    with left:
        st.image("assets/profile.jpg", width=220)

    with right:

        st.markdown("# Shreya Sabale")
        st.markdown("### Business Analyst")

        st.markdown("""
        *Business Analyst exploring how data, systems, and people come together  
        to create better decisions and better outcomes.*
        """)

        st.markdown("""
        Currently working across ERP systems, operational analytics,
        reporting workflows, and business intelligence within manufacturing environments.
        """)

        col1,col2,col3,col4 = st.columns(4)

        with col1:
            st.metric("Functions", "Sales + Marketing")

        with col2:
            st.metric("Tools", "Excel + SQL")

        with col3:
            st.metric("Focus", "Analytics")

        with col4:
            st.metric("Domain", "Manufacturing")

    st.markdown("---")

st.subheader("What I Work On")

c1,c2 = st.columns(2)

with c1:

    st.markdown("""
    ### Business Analytics

    - KPI Tracking & Reporting  
    - Sales & Distributor Analysis  
    - Customer Behaviour Analysis  
    - Sales Projection & Forecasting  
    - Business Growth Analysis  
    """)

    st.markdown("""
    ### Operational Systems

    - ERP Analytics  
    - Dashboard Development  
    - Tracker Creation  
    - Workflow Automation  
    - Data Cleaning  
    """)

with c2:

    st.markdown("""
    ### Production & Operations

    - Production Tracking  
    - Process Visibility  
    - Performance Monitoring  
    - Product Lifecycle Analysis  
    """)

    st.markdown("""
    ### Cross Functional Work

    - Marketing Analytics  
    - HR Policy Work  
    - Export Tracking  
    - Digital Initiatives  
    - Research & Lead Generation  
    """)
    st.markdown("---")

    nav1,nav2,nav3,nav4 = st.columns(4)

    if nav1.button("My Story"):
        st.session_state.page="About"
        st.rerun()

    if nav2.button("Selected Work"):
        st.session_state.page="Projects"
        st.rerun()

    if nav3.button("Certifications"):
        st.session_state.page="Certifications"
        st.rerun()

    if nav4.button("Resume"):
        st.download_button(
            "Download Resume",
            open("assets/resume.pdf","rb"),
            "Shreya_Sabale_Resume.pdf"
        )
# -------------------------------------------------
# ABOUT
# -------------------------------------------------
elif st.session_state.page == "About":

    st.markdown("## 👩‍💼 About Me")

# -------------------------------------------------
# ABOUT
# -------------------------------------------------

elif st.session_state.page == "About":

    st.markdown("## My Story")

    st.markdown("""
A few months ago, I was building projects and searching for opportunities in analytics. 
What started as learning tools gradually turned into understanding how businesses actually function — through systems, people, processes, and data.

Today, I work as a Business Analyst within a manufacturing environment, working across sales, marketing, production, HR, exports, and operational systems. My work often involves creating visibility where complexity exists — whether through dashboards, trackers, reporting workflows, or structured analysis.

What interests me most is understanding how seemingly unrelated pieces connect:

• how operational processes influence decisions  
• how data quality affects business outcomes  
• how systems shape efficiency  
• how structure creates clarity  

Beyond work, I enjoy exploring ideas through volunteering, reading, writing, and experiences that challenge how I think. I see analytics less as a technical skillset and more as a way of observing and understanding the world around me.
""")

    st.markdown("""

### Currently Exploring

• Business intelligence and operational analytics  
• Process improvement through data systems  
• Management education and business strategy  
• Cross-functional problem solving  
• Building analytical workflows that scale  

""")

    # ----- VIDEO SECTION -----

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("### 🎥 Analytical Walkthrough")

    st.write(
        "A walkthrough explaining the thinking, analysis, and decision-making process behind one of my projects."
    )

    st.video("assets/videos/consumption_paradox.mp4")

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("⬅ Back"):
        st.session_state.page = "Home"
        st.rerun()

# -------------------------------------------------
# PROJECTS
# -------------------------------------------------

elif st.session_state.page == "Projects":

    st.markdown("## 📊 Selected Work")

    # -----------------------------------------
    # BUSINESS IMPACT PROJECTS
    # -----------------------------------------

    st.markdown("### Business Impact Projects")

    professional_projects = [

        {
            "title":"Party Master Analysis",
            "impact":"Analysed and standardized 4607+ unique party records, improving customer data visibility, identifying inactive entities, and strengthening reporting accuracy across business functions.",
            "tools":"ERP • Excel • Data Cleaning"
        },

        {
            "title":"Production & KPI Reporting Systems",
            "impact":"Built tracking and reporting systems across multiple production categories, reducing manual monitoring effort and improving visibility for recurring monthly reporting processes.",
            "tools":"Excel • Reporting • Operations"
        },

        {
            "title":"Marketing Workflow Automation",
            "impact":"Designed multiple forms, trackers, and structured workflows supporting daily activity tracking, improving reporting consistency and reducing fragmented data collection processes.",
            "tools":"Google Forms • Sheets • Automation"
        },

        {
            "title":"Sales & Distributor Analytics",
            "impact":"Conducted distributor analysis, repeat enquiry analysis, and sales projections across multiple business segments to improve decision-making visibility for growth initiatives.",
            "tools":"Analytics • Excel • Business"
        },

        {
            "title":"Manufacturing Market Intelligence",
            "impact":"Performed one of the first structured market analyses across manufacturing segments using open-source datasets, industry mapping, RTIs, and lead generation workflows to support expansion activities.",
            "tools":"Research • Analysis • Strategy"
        },

        {
            "title":"Customer Intelligence & Cross Selling Analysis",
            "impact":"Cleaned and analyzed historical datasets spanning 2016–2026, uncovering cross-selling opportunities, repeat business patterns, and active customer segments.",
            "tools":"Data Cleaning • Excel • Analysis"
        }

    ]

    for p in professional_projects:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader(p["title"])

        st.write(p["impact"])

        st.caption(p["tools"])

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")

    # -----------------------------------------
    # INDEPENDENT PROJECTS
    # -----------------------------------------

    st.markdown("### Independent Projects")

    projects = [

        {
            "title": "Job Market Analytics",
            "img1": "assets/dashboards/job_market.jpg",
            "img2": "assets/dashboards/job_market_2.jpg",
            "desc": "Job market trends and skill analysis.",
            "live": "https://job-market-analytics.streamlit.app/",
            "github": "https://github.com/shreya-sabale-sql/job-market-analytics",
            "two_images": True
        },

        {
            "title": "Consumption Paradox",
            "img1": "assets/dashboards/consumption.jpg",
            "desc": "Consumer behavior analysis.",
            "github": "https://github.com/shreya-sabale-sql/consumption-paradox",
            "two_images": False
        },

        {
            "title": "SLA Bottleneck Analysis",
            "img1": "assets/dashboards/sla.jpg",
            "desc": "SLA performance analysis.",
            "github": "https://github.com/shreya-sabale-sql/sql-powerbi-sla-bottleneck-analysis",
            "two_images": False
        },

        {
            "title": "User Funnel Analysis",
            "img1": "assets/dashboards/funnel.jpg",
            "desc": "User journey drop-off analysis.",
            "github": "https://github.com/shreya-sabale-sql/Drop-Off-Rate-User-Funnel-",
            "two_images": False
        },

        {
            "title": "Stock Market Analysis",
            "img1": "assets/dashboards/stock.jpg",
            "desc": "Stock market trend analysis.",
            "github": "https://github.com/shreya-sabale-sql/stock-market-LG",
            "two_images": False
        },

        {
            "title": "Healthcare Digital Transformation",
            "img1": "assets/dashboards/healthcare.jpg",
            "desc": "Healthcare digital transformation case study.",
            "github": "https://github.com/shreya-sabale-sql/healthcare_digital_transformation",
            "two_images": False
        }

    ]

    cols = st.columns(2)

    for i, p in enumerate(projects):

        with cols[i % 2]:

            st.markdown("<div class='card'>", unsafe_allow_html=True)

            st.image(p["img1"], use_container_width=True)

            st.subheader(p["title"])

            if p.get("two_images"):
                st.image(p["img2"], use_container_width=True)

            st.write(p["desc"])

            st.markdown(f"[💻 GitHub Repo]({p['github']})")

            if p.get("live"):
                st.markdown(f"[🚀 View Live App]({p['live']})")

            st.markdown("</div>", unsafe_allow_html=True)

    if st.button("⬅ Back"):

        st.session_state.page = "Home"

        st.rerun()

# -------------------------------------------------
# NOTES ALONG THE WAY
# -------------------------------------------------

elif st.session_state.page == "Blogs":

    st.markdown("## Notes Along The Way")

    entries = [

        {
            "title":"On Not Putting All Eggs In One Basket",
            "text":"""
For a long time, I believed growth meant going deeper into one thing and sticking to it relentlessly.

Over time, that belief started changing.

Working across analytics, business problems, volunteering, reading, writing, and different experiences made me realise that growth is rarely linear. The things that seem unrelated often connect later in unexpected ways.

Learning analytics improved how I think about systems. Volunteering changed how I think about people. Working across functions changed how I think about business.

This phase of life feels less about specialization and more about exploration.

And maybe exploration itself is a form of specialization.
"""
        },

        {
            "title":"Things Work Taught Me Faster Than College",
            "text":"""
Work changed the way I understand business.

In theory, processes are clean.

In reality, data is incomplete, systems are fragmented, priorities change, and people work differently.

Working with ERP systems, customer records, production trackers, dashboards, and reporting workflows taught me that business problems rarely stay inside departmental boundaries.

Sometimes the problem is technical.

More often, it is operational.

And occasionally, it is simply communication.

The more I work, the more I realize that understanding context is often as important as understanding numbers.
"""
        },

        {
            "title":"Why I Started Saying Yes More Often",
            "text":"""
A surprising number of meaningful experiences happened because I stopped waiting to feel ready.

Volunteering as a UPSC scribe.

Working on projects outside my comfort zone.

Taking ownership of systems I had never built before.

Working across departments that initially felt unfamiliar.

Saying yes more often did not always create certainty.

But it created perspective.

And perspective has probably been more valuable than certainty.
"""
        },

        {
            "title":"On Measuring Progress",
            "text":"""
Sometimes progress feels invisible while living through it.

You finish projects.

Build trackers.

Learn tools.

Take on responsibilities.

Move to the next thing.

And then forget how much changed.

Part of why this website exists is because I wanted a place to document what I was learning, building, and struggling with.

Not only for recruiters.

But for future me.

Because growth often becomes visible only in retrospect.
"""
        },

        {
            "title":"Curiosity As A Career Strategy",
            "text":"""
I used to think curiosity was a distraction.

Something that prevented focus.

Now I think the opposite.

Curiosity is probably why I enjoy working across analytics, operations, systems, people, and business problems.

Most interesting problems are interdisciplinary.

Understanding one area often improves understanding of another.

Curiosity may not always create direct answers.

But it consistently creates better questions.
"""
        }

    ]

    for e in entries:

        with st.expander(e["title"]):

            st.write(e["text"])

    if st.button("⬅ Back"):

        st.session_state.page = "Home"

        st.rerun()
# -------------------------------------------------
# CERTIFICATIONS
# -------------------------------------------------
elif st.session_state.page == "Certifications":

    st.markdown("## 🏆 Certifications")

    certs = [
        ("Google Data Analytics", "https://www.coursera.org/account/accomplishments/professional-cert/311AZBGYHD5D"),
        ("SQL for Data Science", "https://www.coursera.org/account/accomplishments/verify/0YVAI3CQALL3"),
        ("Python for Data Analysis", "https://www.udemy.com/certificate/UC-650c93e5-a5a6-419a-a90a-5e1ddd4739a0/"),
        ("Google Data Analytics Capstone", "https://coursera.org/share/018b035389bdce03bc412d5161c33b68"),
        ("Credly Data Analytics Badge", "https://www.credly.com/badges/d52d0240-8973-4a5c-ad03-2f39a44126fb/public_url")
    ]

    for name, link in certs:
        st.markdown(f"🔗 [{name}]({link})")

    if st.button("⬅ Back"):
        st.session_state.page = "Home"
        st.rerun()

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown("---")
st.markdown("<center>Built with ❤️ using Streamlit | Shreya Sabale</center>", unsafe_allow_html=True)

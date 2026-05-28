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
        ### Operational Analytics

        - KPI Tracking  
        - Reporting Workflows  
        - Dashboard Development  
        - Process Visibility  
        """)

        st.markdown("""
        ### Business Systems

        - ERP Analysis  
        - Production Tracking  
        - Automation  
        - Data Cleaning  
        """)

    with c2:

        st.markdown("""
        ### Growth & Marketing

        - Distributor Analysis  
        - Customer Insights  
        - Sales Projection  
        - Marketing Analytics  
        """)

        st.markdown("""
        ### Cross Functional Work

        - Sales  
        - Marketing  
        - HR  
        - Business Reporting  
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

    st.markdown("""
    I enjoy breaking down complex problems and finding clarity through data.
    What draws me to analytics is the ability to transform raw information
    into insights that help make better decisions.

    I work with **SQL, Python, Power BI, and Excel** and enjoy building
    data-driven solutions, dashboards, and analytical models.

    ### How I Think
    • Logical and structured  
    • Curious and analytical  
    • Focused on clarity  
    • Driven by real-world impact  

    ### What I’m Working Towards
    • Strengthening business analytics skills  
    • Working with real datasets  
    • Improving storytelling with data  
    """)

    # ----- VIDEO SECTION -----
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("### 🎥 Project Walkthrough – Consumption Paradox")
    st.write("A short explanation of my analysis and decision-making process.")

    st.video("assets/videos/consumption_paradox.mp4")

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("⬅ Back"):
        st.session_state.page = "Home"
        st.rerun()

# -------------------------------------------------
# PROJECTS
# -------------------------------------------------
elif st.session_state.page == "Projects":

    st.markdown("## 📊 Projects")

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
# BLOGS
# -------------------------------------------------
elif st.session_state.page == "Blogs":

    st.markdown("## ✍️ Blogs & Publications")
    st.markdown("### 📄 White Paper – Indian Economy")

    st.download_button(
        "Download PDF",
        open("assets/white_paper_indian_economy.pdf", "rb"),
        "Indian_Economy_White_Paper.pdf"
    )

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

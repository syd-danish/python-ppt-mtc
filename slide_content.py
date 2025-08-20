VALUATION_DICT = {
    1999: 0.01, 2000: 0.02, 2001: 0.03, 2002: 0.04, 2003: 0.045,
    2004: 0.05, 2005: 0.1, 2006: 0.2, 2007: 0.4, 2008: 0.8,
    2009: 1.0, 2010: 1.5, 2011: 2.0, 2012: 2.5, 2013: 3.0,
    2014: 2.8, 2015: 2.5, 2016: 1.5, 2017: 1.0, 2018: 0
}
JAWBONE_REVENUE_DATA = {
    2010: {
        "revenue": 300,  # Estimated based on growth trajectory before 2011 peak
        "funding": 117,  # Cumulative funding up to 2010 (CB Insights and others)
    },
    2011: {
        "revenue": 500,  # Reported by History Tools as ~$500M driven by headset sales[](https://www.historytools.org/companies/the-real-reason-jawbone-failed-spectacularly)
        "funding": 235,  # Additional funding rounds in 2011
    },
    2012: {
        "revenue": 550,  # Estimated based on Jambox success and market growth
        "funding": 352,  # Cumulative funding including 2011-2012 rounds
    },
    2013: {
        "revenue": 570,  # Estimated based on continued sales of UP and Jambox
        "funding": 472,  # Flat rounds in 2013 (CB Insights)[](https://www.cbinsights.com/research/jawbone-valuation-history/)
    },
    2014: {
        "revenue": 600,  # Reported by CB Insights[](https://www.cbinsights.com/company/jawbone/financials)
        "funding": 622,  # Cumulative including 2014 rounds, valuation at $3.2B[](https://www.cnbc.com/2017/07/10/jawbones-demise-a-case-of-death-by-overfunding-in-silicon-valley.html)
    },
    2015: {
        "revenue": 500,  # Estimated decline due to UP3 issues and market competition
        "funding": 922,  # Includes $300M debt from BlackRock in Q2'15[](https://www.cbinsights.com/research/jawbone-valuation-history/)
    },
    2016: {
        "revenue": 200,  # Estimated sharp decline due to product unavailability and pivot attempts[](https://www.cbinsights.com/research/jawbone-valuation-history/)
        "funding": 1087, # Includes $165M from Kuwait Investment Authority in Q1'16[](https://www.cnbc.com/2017/07/10/jawbones-demise-a-case-of-death-by-overfunding-in-silicon-valley.html)
    },
    2017: {
        "revenue": 50,   # Estimated minimal revenue during liquidation[](https://www.cbinsights.com/research/jawbone-valuation-history/)
        "funding": 1087, # No new funding; company liquidated in July 2017[](https://en.wikipedia.org/wiki/Jawbone_%28company%29)

    }
}

SLIDE_CONTENT={
1:{
        "title":"Jawbone: The Disastrous End of a Silicon Valley Giant",
        "subtitle":"How the pioneer of wireless wearable consumer tech fell from grace"
    }
    ,
2:{
        "title":"The Founders: Fresh Outta Stanford",
         "content":(
    "Alexander Asseily and Hosain Rahman met as graduate students at Stanford University in the late 1990s.\n"
    "Both shared a passion for design, engineering, and emerging consumer technology.\n"
    "Their collaboration began with class projects exploring wearable tech and human–computer interaction.\n"
    "This partnership would lay the foundation for Aliph, the company that would later be rebranded as Jawbone."
)
    },
3:{
         "title":"Aliph: A humble initial goal",
"content":("Jawbone, was originally founded as Aliph or AliphCom, Inc. by two fresh stanford university graduate"
" in 1999 with a simple goal to suppress external noises during phone calls\n"
"In 2002, They received special permission to research noise cancellation"
" from DARPA and the US Navy with military technology within the Lawrence Livermore National Laboratory and"
" in 2004, They released their first product: A noise cancellation headset")
    },
4:{
          "title":"Early recognition",
"content":(
    "Aliph's very first product received instant recognition within Silicon Valley"
    ", earning them a design award and deals with tech giants like Apple "
    "which only encouraged their innovation. A Bluetooth version of their original product"
    " which would be named 'Jawbone' in 2006"
)

    },
5:{
           "title":"Expanding the range",
"content":("By 2010, Aliph had renamed itself after it's star product but sought to broaden\n"
                     "The same year, Jawbone launched the Jambox portable Bluetooth speaker."
                     " Its beautiful design and sound quality quickly turned it into a hit.\n"
                     "The next year, Jawbone introduced the UP wrist-worn fitness tracker, "
           "entering the burgeoning wearable health space.\n")},
7:{
        "title":"Cracks and Competition: The Beginning of the End",
        "subtitle":("Jawbone’s momentum starts to falter under market pressure,"
                               " product flaws, and operational strain and multiple other factors"
                               " which would sooner or later come to light.")

    }
    ,
8:{
            "title":"The Beginning of the Downfall",
"content":(
    "By the early 2010s, Jawbone was no longer the only sleek, design-focused player in wearable tech. "
    "Competitors like Fitbit, Garmin, and eventually Apple began offering devices with broader ecosystems, "
    "better battery life, and aggressive pricing. "
    "Jawbone’s premium, design-led strategy suddenly looked expensive and limited.\n"
    "The market shift forced Jawbone into a race it wasn’t prepared for — while their products still won "
    "design awards, rivals were winning on functionality, reliability, and integration with health platforms."
)
    },
9:{
             "title":"Product Faults and Consumer Backlash",
"content":(
    "Jawbone's once-celebrated products began to show cracks — literally and figuratively. "
    "The UP fitness bands suffered from battery failures, syncing issues, and fragile build quality. "
    "Many units broke within weeks, forcing Jawbone into costly replacement programs.\n"
    "Software updates often lagged behind competitors, leaving users frustrated. "
    "These reliability problems damaged brand trust just as the wearables market was exploding, "
    "pushing customers toward more dependable options like Fitbit and Apple Watch."
)

    },
10:{
               "title":"Operational and Financial Strain",
"content":(
    "By 2015, Jawbone was in crisis mode. Recalls, replacements, and declining sales "
    "burned through cash reserves. The company faced multiple production delays and "
    "could not keep pace with the rapid product cycles of its rivals.\n"
    "Investors grew impatient, and fundraising became increasingly difficult despite "
    "Jawbone having raised nearly $1 billion over its lifetime. Leadership churn, "
    "supply chain disruptions, and mounting lawsuits further drained resources.\n"
    "The once high-flying startup was now locked in a costly, unsustainable fight to "
    "stay relevant in a market it had helped create."
)
    },
11:{
"title":"More in, less out: the reasons for the financial dilemma",
"content":("Excessive R&D spending without immediate returns.\n"
    "High operational costs and rapid team expansion.\n"
    "There were many faults within the Jawbone UP product which was launched to compete with the Fitbit\n"
    "Inability to secure sustainable revenue streams.\n"
    "Increasing investor pressure after years of losses.\n"
    "By 2016, funding dried up as confidence in the brand eroded.")
    },
12:{
"title":"A broken health tracker: the faults of Jawbone UP ",
"content":("Hardware Issues: Early UP bands (2011-2012) suffered from widespread hardware failures, including cracking bands and dead batteries, leading to a full product recall in 2011\n"
"Syncing and Connectivity Problems: UP and UP24 models frequently failed to sync with mobile apps, frustrating users with inconsistent data tracking (reported by ~30% of users in 2013 reviews).\n"
"Inaccurate Heart Rate Monitoring: UP3 (2015) heart rate sensors were unreliable, often providing erratic or missing readings compared to competitors like Fitbit.\n"
"Waterproofing Failures: UP3 and UP4 were marketed as water-resistant but failed under minimal water exposure, leading to device malfunctions (noted in 2015 consumer complaints).\n"
"Short Battery Life: UP devices had battery life as low as 3-5 days versus advertised 7-10 days, significantly worse than competitors by 2014.\n"
"Software Bugs: Jawbone’s app was plagued by crashes and data loss, with frequent user reports of lost sleep and activity tracking data in 2014-2015.\n")
    },
13:{"title":"The falling public perception",
        "content":("Poor Customer Support: Users complained that customer service was slow, dismissive, or unhelpful."
"Warranty replacements were common, but turnaround times were long. Many users reported unresponsive "
"customer support, with long wait times and unfulfilled refunds by 2016.\n"
"The media factor: Rumors about financial instability leaked into the press — consumers started doubting whether Jawbone products would be supported long-term."
"Competitors like Fitbit and Apple appeared stable and dependable, further eroding trust.\n"
"Product Reliability and Quality Issues: Frequent returns and replacements led to frustration."
"Reports of devices breaking within weeks or months.")},
14:{"title":"The Desperate pivots: A not so 'jawdropping' response",
    "content":("Product Recalls and Refunds: Jawbone offered refunds and replacements for faulty UP fitness trackers, costing millions\n"
    "Iterative Product Launches: Jawbone also released UP2, UP3, and UP4 (2014-2015) to address hardware issues, but core problems persisted even in the later versions.\n"
    "Legal Action Against Fitbit: Sued Fitbit in 2015 for alleged trade secret theft, "
    "diverting resources from product fixes but eventually lost the legal battle which led to public embarrassment and perceptions of corporate mismanagement.\n"
    "Pivot to Health Data Services: Attempted a shift to medical-grade wearables and health data platforms in 2016, "
    "but their execution in every realm was weak.\n"
    "Layoffs and Cost-Cutting: Implemented multiple layoffs by 2016 to manage "
    "financial strain from declining sales")},
15:{"title":"Jawbone’s Internal Struggles and Workplace Issues",
    "content":("Leadership Challenges: Hosain Rahman pushed Jawbone into too many "
                   "markets (headsets, speakers, wearables, health tech) without clear focus. His Leadership style described as demanding and controlling, "
                   "which alienated both senior executives and employees.\n"
                   "Toxic Workplace Allegations: High executive turnover due to clashes with Rahman’s leadership style. "
                   "Unrealistic timelines and constant “fire drills” created an unsustainable work environment as well as allegations of favoritism and internal politics, "
                   "all of which lead to an overall low morale within the company.")},
16:{"title":"The liquidation and end of jawbone",
        "content":("By 2017, Jawbone had reached the end of its turbulent journey. Mounting debts, relentless competition from Fitbit and Apple, "
                   "and years of strategic missteps left the company unable to sustain itself. "
                   "In July of that year, Jawbone entered liquidation, "
                   "marking one of the largest failures in the history of consumer electronics startups."
                   "Jawbone’s downfall became a cautionary tale of how over-ambition, leadership flaws, "
                   "and internal chaos can destroy even the most well-funded and innovative companies.")},
17:{"title":"Conclusion",
        "content":("Jawbone’s story is a cautionary tale in Silicon Valley history. Despite billions in funding and early technological promise, the company crumbled under the weight of poor leadership, toxic culture, and its inability to adapt to an evolving market. Its downfall underscores the importance of sustainable innovation, "
                  "healthy internal culture, and strategic focus—reminding us that ambition alone cannot guarantee success.")}
}
BIG_JAMBOX="https://www.blessthisstuff.com/imagens/listagem/2012/grande/grande_jawbone-big-jambox.jpg"
JAMBONE_UP24="https://www.cardiofitness.de/cdn/shop/files/jl0152seu1-up24_mix_800_2014.jpg?v=1689300343&width=640"
JAWBONE_HEADSET="https://www.zdnet.com/a/img/2014/10/04/72281353-4b97-11e4-b6a0-d4ae52e95e57/jawbone-2-1.jpg"
JAWBONE_TEAM="https://media.gettyimages.com/id/491588012/photo/san-francisco-ca-shervin-pishevar-hosain-rahman-and-designer-yves-behar-attend-the-vanity-fair.jpg?s=612x612&w=0&k=20&c=IjkTkhhgEPS3FFw3_7WkteNUgxPRR1qQ9DEHwjQa8HI="
ALEXANDER_ASSEILY="https://alchetron.com/cdn/alexander-asseily-34f81526-f1a1-45e8-8fff-c2d8739c734-resize-750.jpg"
HOSAIN_RAHMAN="https://media.gettyimages.com/id/488312819/photo/hosain-rahman-chief-executive-officer-of-jawbone-speaks-during-the-techcrunch-disrupt-nyc-2014.jpg?s=612x612&w=0&k=20&c=tryKCuvj47b1VurTHS9UMh_G1pNJNgDCxB2xzzwOZdY="
JAWBONE_VS_FITBIT="https://www.cnet.com/a/img/resize/622c668562813758579f50ab822a978e9230166c/2013/06/28/30024016-e467-11e2-8339-d4ae52e62bcc/JawBonevsFitBitFlex.jpg?auto=webp&fit=crop&height=110&width=196"
JAWBONE_FITBIT_LAWSUIT="https://static01.nyt.com/images/2015/05/27/business/document-jawbone-sues-fitbit/document-jawbone-sues-fitbit-videoLarge.png"
#JAWBONE_WEBSITE="https://ichef.bbci.co.uk/ace/standard/976/cpsprodpb/69A4/production/_96844072_mediaitem96844071.jpg"
APPLE_HEALTH_WATCH="https://cdsassets.apple.com/live/7WUAS350/images/health/ios-17-iphone-14-pro-watchos-10-series-8-health-heart-rate.png"
JAWBONE_UP_SERIES="https://cdn.mos.cms.futurecdn.net/M2WChkMYfAPqZ4EvVtukvk.jpg"
JAWBONE_HEALTH_LOGO="https://logodix.com/logo/1276536.png"
IMAGE_URL=[BIG_JAMBOX,JAMBONE_UP24,JAWBONE_HEADSET
    ,JAWBONE_TEAM,ALEXANDER_ASSEILY,HOSAIN_RAHMAN,JAWBONE_VS_FITBIT,JAWBONE_FITBIT_LAWSUIT
    ,APPLE_HEALTH_WATCH,JAWBONE_UP_SERIES,JAWBONE_HEALTH_LOGO]



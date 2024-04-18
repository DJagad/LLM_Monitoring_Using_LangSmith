from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are the helpful assistant. Please Respond to the user request only based on the given context"),
        ("user","Question:{question}\nContext:{context}")
    ]

)

model = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt| model | output_parser

question = "Can you summarize the speech?"
context = """Distinguished Guests

Ladies and Gentlemen.

It is both an honour and a pleasure for me to be in your midst in the historic capital city of Sofia. Bulgaria is an ancient land, with a long history and a glorious cultural heritage. We know of its literary, philosophical and cultural tradition. The statue of Sofia, in the Centre of this beautiful city, holding the symbols of fame and wisdom in her hands and wearing the crown of the Goddess of fate truly characterizes the aspirations of all mankind.

India and Bulgaria have a long-standing friendship. Both have ancient civilizations and our histories have involved contacts with numerous other societies. We have been able to benefit from this by assimilating in our cultures various facets of other civilizations. This has enabled the development of India's and Bulgaria's multi-culturalism drawn from different religious, ethnic and linguistic groups. This is an abiding gift from our previous generations, which we in turn are preserving for the future.

India and Bulgaria have always had wide-ranging contacts between our Governments and our people. Our co-operation is multi-dimensional and extends to the realms of politics, trade and economics, science and technology and culture. This relationship is based on continuity and mutual understanding. The exchange of Presidential Visits in 1994 to Sofia and in 1998 to New Delhi has provided the momentum to strengthen and broad base our contacts. My own visit here is in continuation of these high-level exchanges and we hope that it will serve to further enhance our bilateral co-operation. Time has come both Bulgaria and India should identify the core competence in specific areas and select projects of importance for joint design, development, production and marketing in a time-bound manner. I am glad that both countries have identified a number of scientific research projects under the Indo-Bulgarian Science & Technology cooperation. Excellency, I am confident that Indo-Bulgarian Partnership has a bright future.

In the new millennium, the entire world is moving in the direction of free and democratic systems. India and Bulgaria share these values. In our own experience of the last fifty years and more, we have found the democratic par liamentary system an appropriate vehicle for serving the needs and aspirations of our people. As with the polity, the current century is seeing a general consensus on the need to undertake structural economic reforms to open up possibilities for enhancement of the welfare of the people of this planet. In India, we are proceeding with the second generation of our economic reforms and are happy to see the success that we have been able to obtain. India is increasingly recognized as a global economic power with notable successes in the frontier areas of information technology, science, space technology and in newly emerging technologies such as nano and bio technology. We have seen that Bulgaria has undertaken major steps in the process of liberalization and has rapidly moved towards a free market economy. I am sure that this will open up opportunities for further extending our economic and commercial ties. The high value attached to education in both our countries and the strong human capital base that we have been able to build up will definitely strengthen mutually beneficial co-operation. Our two way business is presently very limited. We should enhance our trade and business to billion dollars in a few years time. In India, we believe that the fruits of economic progress should be widely available, especially to the under-privileged sections of our population. The world still has a lot to do for eradication of poverty, unemployment and disease; this shared responsibility must be borne by the global community as a whole.

In the realm of international affairs, we too need to address the question of attainment of an equitable world order. We are happy to see that the international community is, indeed, making efforts for such a just system based on respect for sovereignty and territorial integrity of States. The United Nations should function as a true international body and empowered by all members to lead to cohesive conclusions and actions. At the same time, Excellency, as you are aware, new challenges and threats have emerged. The most serious issue we are currently confronted with is that of international terrorism. Terrorism has become a major force jeopardizing international peace and security. It would seem that no State or people are free from this danger. Both India and Bulgaria have a common perception on the dangers posed by this menace. The international community has to take concerted action to isolate and eliminate the sources of such terrorist acts, the impact of which has been felt, by innocent victims including women and children. No terrorist act can be justified on any ground whatsoever. I hope, Excellency, that we shall continue to work jointly and with renewed vigour to eliminate this scourge from the globe.

The Bulgarian and Indian people have had close contacts. The great Bulgarian revolutionary Georgi Rakovski has written that "The oldest civilization in the world was that of India and different beliefs and customs originated from it". The works of Gandhi, Tagore and Nehru have been translated into Bulgarian and have been popular here. Bulgarian poets Hristo Botev and Hristo Smirenski have exercised influence on Indian writers. During the 19th century, Bulgarian literature reflected the national consciousness and patriotic sentiments as did the writings in India during our freedom struggle. The contacts in the cultural sphere continue and I know that many Bulgarians travel to India to study literature, dance, music and philosophy. I was very happy to note that the Sofia University has a separate Indology Department which offers courses in the languages, history and philosophy of India. The interest amongst Bulgarians in Indian classical music, yoga and ancient Indian scriptures are only some of the aspects of Indian society that have been absorbed in this country. I am also glad to learn that Bulgarian Sportsmen and coaches have been training Indian sportspersons who get the benefit of the experience of your great sporting nation.

From our side we could suggest some new areas of cooperation in which India has gained experience. These could include pharmaceuticals, food processing, power and also a sharing of our experience of privatisation. I am optimistic that flourishing economic and scientific ties will take more and more Indians and Bulgarians to each other's country and forge our bonds of friendship further.

Excellency, I would like to take this opportunity to convey my personal greetings and that of my delegation for the warm and friendly hospitality that has been accorded by you. This is in keeping with the time-honoured tradition of Bulgaria and its great people. It is also a reflection of the regard with which India is held in this beautiful country."""

print(chain.invoke({"question":question,"context":context}))
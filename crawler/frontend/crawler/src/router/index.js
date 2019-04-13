import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Crawler from '@/components/Crawler'

Vue.use(Router)
// const API_URL = 'http://127.0.0.1:5000/api'

// export function fetchSurveys() {  
//   return axios.get(`${API_URL}/surveys/`)
// }

// export function fetchSurvey(surveyId) {  
//   return axios.get(`${API_URL}/surveys/${surveyId}/`)
// }

// export function saveSurveyResponse(surveyResponse) {  
//   return axios.put(`${API_URL}/surveys/${surveyResponse.id}/`, surveyResponse)
// }

// export function postNewSurvey(survey) {  
//   return axios.post(`${API_URL}/surveys/`, survey)
// }



export default new Router({
  routes: [
    {
      path: '/crawler',
      name: 'Crawler',
      component: Crawler
    },
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ]
})

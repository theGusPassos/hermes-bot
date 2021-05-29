(ns hermes-api.service
  (:require [io.pedestal.http.route :refer [expand-routes]]))

(def common-interceptors [])

(defn respond-hello [request]
  {:status 200 :body "Hello =)"})


(def default-routes
  #{["/api"
     :get (conj common-interceptors
                respond-hello)
     :route-name :test]})

(def routes
  (expand-routes default-routes))
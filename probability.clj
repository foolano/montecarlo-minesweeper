(def  default-board-size 9) ; default-board-size x default-board-size
(def  default-number-mines 10) ; default-board-size x default-board-size
(def  default-number-samples 1000000) ; default-board-size x default-board-size

(defn new-mine [board-size current-mines]
  (let [mine-pos [(rand-int board-size), (rand-int board-size)]]
    (if (contains? current-mines mine-pos)
      (new-mine board-size current-mines)
      mine-pos)))

(defn generate-mines [board-size num-of-mines]
  (loop [i num-of-mines mines #{}]
    (if (> i 0)
      (recur (dec i) (conj mines (new-mine board-size mines)))
      mines)))

(defn has-adjacent? [pos mines]
  (let [x (pos 0) y (pos 1)]
    (cond
      (contains? mines [(+ x 1) y]) true
      (contains? mines [(- x 1) y]) true
      (contains? mines [x (+ y 1)]) true
      (contains? mines [x (- y 1)]) true
      (contains? mines [(+ x 1) (+ y 1)]) true
      (contains? mines [(+ x 1) (- y 1)]) true
      (contains? mines [(+ x 1) (+ y 1)]) true
      (contains? mines [(- x 1) (- y 1)]) true
      :else false)))

(defn all-adjacents? [mines]
  (every? #(has-adjacent? % mines) mines))

(defn random-var-function [mines]
  (if (all-adjacents? mines)
    1
    0))

(prn
  (float
    (/
      (reduce
        +
        (map
          random-var-function
          (repeatedly default-number-samples (fn [] (generate-mines default-board-size default-number-mines)))))
      default-number-samples)))

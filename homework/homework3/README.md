# Final problems

1. **Dynamic programming**

  Create a simple 8 X 1 grid world, such that the reward in every entry is -1 except for the `home` square in the top which has a reward of 0. In this world the possible moves are up or down. Moving down in the bottommost square keeps you in the same square. If you reach the `home` square, then you automatically `win` and receive the `0` reward – i.e. once you reach `home` you can never move out of it.

  a. **Policy Evaluation**: Assume a random policy – i.e. your probability of moving up or down is 0.5 in every square. Use dynamic programming to find the value function for this policy. Use the Bellman equation explicitly and iteratively to find the value for each square. After each iteration you will get closer and closer to correct value function.

  b. **Policy iteration**: Now use dynamic programming to find the optimal policy. Start with a random policy, as in (a). Perform policy evaluation , as in (a), until it converges. Now update the policy based on this value function by being greedy – for each square, update your policy by assigning a probability of 1 to the action (up/down) according to whichever action has a higher expected value. If both actions would result in equal expected values, assign them equal 0.5 probabilities. Then repeat policy evaluation again, using this new policy. Keep iterating between policy evaluation and policy

  c. Repeat (b) but don’t do policy evaluation until it converges. Just iterate policy evaluation 2 twice each time. Then repeat policy evaluation and policy improvement until you converge on the optimal policy (and expected value function).

2. **Reinforcement learning**

  Use the same grid world as in (1), but learn the optimal policy using Q-learning.
  Here you will learn the optimal state-action function (`Q(x,u)`).
  The idea is to move around the world probabilistically according to the `softmax`
  function – i.e. if all state-action pairs have the same expected value, then you have   equal probability of choosing each action from that state. Then, based on the rewards you experience, update the state-action function according to the update equation we  went through in class.

3. **Optimal control for scalar dynamical system in discrete time**

  Take the dynamical system: `x_(t+1) = a * x_t + b * u_t`

  with cost function: `g(x,u) = q * x^2 + r * u^2`

  Find the control policy: `u = -k * x` which minimizes the expected total cost for the trajectory. Use the values: `a = .8; b = 1; q = 1; r = 1.`

  a. Find the recursive Riccati equations for the gain for this system. This should be the equations in the lecture (if I got it down right) for `p`. You can also derive them again by i) express the total cost to go using the recursive Bellman equation, ii) assume that the optimal value function has a quadratic form `V* = p * x^2`, iii) substitute this into the Bellman equation, iv) minimize this with respect to u to find the optimal control policy, v) substitute `u*` into the Bellman equation and solve for the gain `p`.

  b. Find the steady state optimal control gain, using the Riccati equation. The equation gives `p_(t-1) = f(p_t)`. So initialize `p(T) = q(T)` , where `T` is the final time and `q(T)` is the cost at the final time. Then iterate the Riccati equations backwards until you reach a steady state value. Plot the evolution of `p` over iterations.

  c. Do control. Choose an arbitrary starting state for `x` and then evolve your system over time, as dictated by the equations above. At each time step calculate the `u*` according to the optimal control gain found using the Riccati equations above.

  d. Find the same gains by brute force. Go sequentially through a series of different gains (either p or k), simulate the system as in (c) above and calculate the cost for each trajectory. Find the trajectory with the minimal cost. Compare the corresponding gain with that calculated using the Riccati equations above.

  e. (optional) Find the same gains using matlab. Use the functions `dlqr` and `dare` (discrete time LQR control, discrete time algebraic riccati equations) with the system parameters to find the optimal gains. Compare with the results from above.

4. **Optimal estimation using Kalman filtering**

  Take second order dynamical system in discrete time:

  ```
  x_(t+1) = A * x_t + B * u_t + w_t
  y_t = C * x_t + v_t
  ```

  with `E(w_t * w_t.T) = Q` and `E(v_t * v_t.T) = R`.

  Find the recursive update equations to do optimal estimation, consisting of the iterative steps (b,c,d) below. Use the difference equation:

  ```
  x_t+2 + 0.9 * x_t+1 + 0.1 * x_t = u_t
  ```

  You should simulate the dynamical system above, propagating the state according the update equation, generating random noise at each iteration (use the multivariate normal function mvnrnd – or just use `normrnd` for each dimension separately and assume that `Q` and `R` are diagonal). Choose different values of Q and R to examine effects of measurement and process noise.

  a. Choose arbitrary initial guesses for `x` and the confidence in `x`, given by the error covariance `Sigma0`.

  b. Propagate the estimates forward in time to get a prediction of the state. These are the equations involving the state transition matrix `A`.

  c. Calculate the Kalman gain.

  d. Update the estimates, using the new measurement `y_t` and the predictions found in b.

  e. Repeat the steps b-d as your system evolves. Plot the actual state of the system vs. the state predicted in d, along with the measurements – how much does the estimate pay attention to the measurement noise? Use different values for the measurement noise R to see how the filter switches between being data driven vs. prediction driven. Use different system dynamics to simulate different systems, or add a control signal in there as well to see how it tracks.

5. **OPTIONAL: Optimal control for continuous time, second order system**

  Take the second order system:

  ```
  a + b * v + k * x = u
  ```

  with acceleration `a`, velocity `v`, position `x`, and driving force `u`, and stiffness `k` and damping `b`. Use the values: `k = 10`, `b = -0.2`. Express the system in state space form:

  ```
  dx/dt = A * x + B * u
  ```

  (x is a 2 x 1 vector with position and velocity, `A` is a 2 x 2 matrix with elements
    of 0 1 and b and k, B is a 2 x 1 vector and u is a scalar). Assume quadratic cost function:

  ```
  g(x,u) = x.T * Q * x + u.T * R * u
  ```

  Find the optimal control policy `u* = -K * x` to minimize the above cost.

  Do a – d as above. You need the continuous time Riccati matrix equations. We did not cover this in class so you will need to find them. The principle is the same as the DT case though. In this case the Ricatti equations will be a differential equation that calculates the Riccati coefficients, starting from the terminal state then going backwards. This will be a differential equation `Pdot = f(P,A,B,Q,R)`. The procedure is the same though: choose initial conditions `P = Q(T)`, then evolve the system backwards in time using the differential equation – you need to use one of matlab’s differential equation integrators (ode45 should be good) to evolve the system. Give it enough time to reach steady state. Then use this gain to calculate the control gain, using the equations from the lecture. Simulate the system with these gains (again using `ode45` to simulate the system dynamics).


  Then figure out the optimal control gains using brute force – `K` is a `2 x 1` vector so go through a series of possible gains (e.g `K(1) = 0:.1:3` and `K(2) = 0:.1:3`) and evaluate the system for each of these gains.

  Compare the gains found using each method.



# Potential project

First, you can do a project as I originally proposed. I've put a document in Canvas
summarizing some potential ideas. If you decide to go this route, you have to
let me know your topic by the end of the week. Please do this even if you've
talked to me informally about this previously.

Second, you can do a problem set on reinforcement learning and optimal control/estimation.
This will be a bit more sprawling than the first two problem sets (probably 5-6 problems)
but will be more constrained with well defined problems.

1. **Learn control of dynamic system**
  - use q-learning (simple) or more complicated reinforcement learning techniques to
  control a limb simulation
    * simulate 2-dof limb (just use joint torque controls to make it easier, though
it would probably also be fine to just do something easier, like a single dof
  - could also use different techniques to do adaptive control (model reference control,
distal supervised learning, feedback error learning, neural nets and backprop).
We didn’t cover these in class though.

2. **Apply density estimation using mixture of Gaussians** for real data sets
(e.g. for EMG pattern recognition, for neuron action potentials)

3. **Replicate the Zipser and Andersen article** (see also Mazzoni et al PNAS)

4. **Do the Kohonen net in the Graziano paper** (or a version thereof) or for other cortical models

5. **Implement Kalman filter on an experimental dataset**

6. **2/3 power law**
  - replicate the Gribble and Ostry or Schaal and Sternad results. Simulate
  multi-degree of freedom limb (should work with 2dof), put realistic muscles on the limb,
  drive each joint angle with sinusoids, see whether 2/3 power law comes out.

7. **Build EP control** (ala Gribble J Neurophys article)

8. **simulate equilibrium point control of point to point movements**, using either
alpha or lambda models, simulate 2dof limb with ‘spring-like’ muscles, specify virtual
trajectory (or simply the final end point), and move to the final position.

9. **Use something like Hebb’s rule to simulate development of Ia reflex pathways**

  - one idea is that Ia reflex strength (heteronymous reflexes) result from the similarity
  of mechanical actions of muscles, this would imply that muscles that are stretched
  at the same time should be the ones with reflex effects. You could do this with
  different muscle anatomies to see how it changes.
  - Biol Cybern. 1994;70(5):417-25.
  - An unsupervised neural network model for the development of reflex co-ordination.
  - Smeets JB, van der Gon JJ.

10. **Perform simulations from Todorov using LQG**
  - Could choose a subset
  - Could see if using multiplicative noise was necessary (e.g. just use LQG instead)
  - Just redo one of their toy problems with stochastic control could also do muscles),
  implement q-learning or other technique to learn limb control or point mass along
  a trajectory – e.g. like the toy problems in Todorov

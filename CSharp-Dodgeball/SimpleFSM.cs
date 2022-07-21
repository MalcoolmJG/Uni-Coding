using UnityEngine;
using System.Collections;

public class SimpleFSM : MonoBehaviour 
{
    public enum FSMState
    {
        None,
        Patrol,
		Dead,
		Chase,
		Attack
    }

	// Current state that the NPC is reaching
	public FSMState curState;

	public float moveSpeed = 12.0f; // Speed of the tank
	public float rotSpeed = 2.0f; // Tank Rotation Speed
	public float turretRotSpeed = 3.0f;
	
	protected Transform playerTransform;// Player Transform
	protected Vector3 destPos; // Next destination position of the NPC Tank
	protected GameObject[] pointList; // List of points for patrolling
	
    // Whether the NPC is destroyed or not
    protected bool bDead;
    public int health = 100;

	// Effects for death
	public GameObject explosion;
	public GameObject smokeTrail;

	//tank ranges
	public bool chase = true; // whether chaser will chase or not
	public float chaseDist = 25.0f; // if target within this distance, chaser will chase
	public float attDist = 20.0f; // if target within this range, tank will attack
	public float stopDist = 10.0f; // if target within this distance, chaser will stop
	private Rigidbody _rigidbody; // The rigidbody of the chaser

	public GameObject turret;
	public GameObject bullet;
	public GameObject bulletSpawnPoint;
	//Bullet shooting rate
	public float shootRate = 1.5f;
	protected float elapsedTime;

    /*
     * Initialize the Finite state machine for the NPC tank
     */
	void Start() {
        curState = FSMState.Patrol;

        bDead = false;

        // Get the list of patrol points
        pointList = GameObject.FindGameObjectsWithTag("PatrolPoint");
		FindNextPoint();  // Set a random destination point first

        // Get the target (Player)
        GameObject objPlayer = GameObject.FindGameObjectWithTag("Player");
        playerTransform = objPlayer.transform;
        if(!playerTransform)
            print("Player doesn't exist.. Please add one with Tag named 'Player'");

	}


    // Update each frame
    void Update() {

        switch (curState) {
			case FSMState.Patrol: UpdatePatrolState(); break;
			case FSMState.Dead: UpdateDeadState(); break;
			case FSMState.Chase: UpdateChaseState(); break;
			case FSMState.Attack: UpdateAttackState(); break;
        }
		if(Vector3.Distance(transform.position, playerTransform.position) <= attDist){
			curState = FSMState.Attack;
		}else if (Vector3.Distance(transform.position, playerTransform.position) <= chaseDist) {
			curState = FSMState.Chase;
		}

		// Go to dead state if no health left
        if (health <= 0)
            curState = FSMState.Dead;


		 
	
	}


	//chase state
	protected void UpdateChaseState(){

//		float distance = Vector3.Distance(transform.position, playerTransform.transform.position);

		Quaternion targetRotation = Quaternion.LookRotation(playerTransform.position - transform.position);
		GetComponent<Rigidbody>().MoveRotation(Quaternion.Slerp(transform.rotation, targetRotation, Time.deltaTime * rotSpeed));  

		// Go Forward
		GetComponent<Rigidbody>().MovePosition(GetComponent<Rigidbody>().position + transform.forward * Time.deltaTime * moveSpeed);
	}

	//Attack State
	protected void UpdateAttackState(){
	if (elapsedTime >= shootRate)
	{
		//Reset the time
		elapsedTime = 0.0f;

		//Also Instantiate over the PhotonNetwork
		if ((bulletSpawnPoint) & (bullet))
			Instantiate(bullet, bulletSpawnPoint.transform.position, bulletSpawnPoint.transform.rotation);
	}}


	/*
     * Patrol state
     */
    protected void UpdatePatrolState() {
        // Find another random patrol point if the current point is reached
        if (Vector3.Distance(transform.position, destPos) <= 2.0f) {
            FindNextPoint();
        }
      
        // Rotate to the target point
        Quaternion targetRotation = Quaternion.LookRotation(destPos - transform.position);
        GetComponent<Rigidbody>().MoveRotation(Quaternion.Slerp(transform.rotation, targetRotation, Time.deltaTime * rotSpeed));  

        // Go Forward
		GetComponent<Rigidbody>().MovePosition(GetComponent<Rigidbody>().position + transform.forward * Time.deltaTime * moveSpeed);
    }


	
    /*
     * Dead state
     */
    protected void UpdateDeadState() {
        // Show the dead animation with some physics effects
        if (!bDead) {
            bDead = true;
            Explode();
        }
    }


	// Find the next semi-random patrol point
    protected void FindNextPoint() {
        int rndIndex = Random.Range(0, pointList.Length);
		destPos = pointList[rndIndex].transform.position;
    }


	// Check the collision with the bullet
	void OnCollisionEnter(Collision collision) {
		// Reduce health
		if(collision.gameObject.tag == "Bullet")
			health -= collision.gameObject.GetComponent<Bullet>().damage;
	} 


    protected void Explode() {
        float rndX = Random.Range(8.0f, 12.0f);
        float rndZ = Random.Range(8.0f, 12.0f);
        for (int i = 0; i < 3; i++) {
            GetComponent<Rigidbody>().AddExplosionForce(10.0f, transform.position - new Vector3(rndX, 2.0f, rndZ), 45.0f, 40.0f);
            GetComponent<Rigidbody>().velocity = transform.TransformDirection(new Vector3(rndX, 10.0f, rndZ));
        }

		if (smokeTrail) {
			GameObject clone = Instantiate(smokeTrail, transform.position, transform.rotation) as GameObject;
			clone.transform.parent = transform;
		}
		Invoke ("CreateFinalExplosionEffect", 1.4f);
		Destroy(gameObject, 1.5f);
	}
	
	
	protected void CreateFinalExplosionEffect() {
		if (explosion) 
			Instantiate(explosion, transform.position, transform.rotation);
	}

	void ApplyDamage(int dmg) {
		health -= dmg;
	}

	}

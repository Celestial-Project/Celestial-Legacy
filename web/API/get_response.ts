interface ChatResponse {
  chat: string;
}

const get_response = async (message: string = "", debug: boolean = false): Promise<string> => {

    const response = await fetch('http://celestialapi.trueddns.com:21250/celestial-api', {
      method: 'POST',
      mode: 'cors',
      cache: 'no-cache', 
      credentials: 'same-origin', 
      headers: {
        'Content-Type': 'application/json',
        'Accept': '*/*'
      },
      redirect: 'follow', 
      referrerPolicy: 'no-referrer',
      body: JSON.stringify({
        message: message
      })
    })

    const data: ChatResponse = await response.json()

    if (debug){
      console.log(data)
    }
    
    return data.chat

}

export default get_response
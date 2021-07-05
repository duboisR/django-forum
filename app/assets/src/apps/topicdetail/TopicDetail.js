import React, { useState, useEffect } from 'react';
import jsonFetchData from './api';


//  Components
const TopicSideBar = ({filter, setFilter}) => {
    return (
        <div className="inner-wrapper">
            <div className="inner-sidebar">
                <div className="inner-sidebar-header justify-content-center">
                    <a className="btn btn-primary has-icon btn-block" href="/topics/new/">New topic</a>
                </div>
                <div className="inner-sidebar-body p-0">
                    <div className="p-3 h-100" data-simplebar="init">
                        <nav className="nav nav-pills nav-gap-y-1 flex-column">
                            <a href="#" onClick={() => setFilter("all")} className={`nav-link nav-link-faded has-icon ${filter == 'all' ? "active" : ""}`}>
                                All Threads
                            </a>
                            <a href="#" onClick={() => setFilter("solved")} className={`nav-link nav-link-faded has-icon ${filter == 'solved' ? "active" : ""}`}>Solved</a>
                            <a href="#" onClick={() => setFilter("unsolved")} className={`nav-link nav-link-faded has-icon ${filter == 'unsolved' ? "active" : ""}`}>Unsolved</a>
                            <a href="#" onClick={() => setFilter("noreplies")} className={`nav-link nav-link-faded has-icon ${filter == 'noreplies' ? "active" : ""}`}>No replies yet</a>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
    )
}

const TopicHeader = ({search, setSearch}) => {
    const [searchInput, setSearchInput] = useState(search);

    return (
        <div className="inner-main-header">
            <span className="input-icon input-icon-sm ml-auto w-auto">
                <form onSubmit={(event) => {event.preventDefault(); setSearch(searchInput);}}>
                    <div className="form-row align-items-center">
                        <div className="col-auto">
                            <input type="text" name="search" className="form-control bg-gray-200 border-gray-200 shadow-none"
                                placeholder="Search forum" onChange={(event) => setSearchInput(event.target.value)} value={searchInput} />
                        </div>
                        <div className="col-auto">
                            <input type="submit" className="btn btn-primary has-icon btn-block" value="Search" />
                        </div>
                    </div>
                </form>
            </span>
        </div>
    )
}

const TopicMessage = ({message}) => {
    return (
        <div className="card mb-2">
            <div className="card-body">
                <div className="media forum-item">
                    <a href="#" className="card-link">
                        <img src={message.creator_serializer.avatar_url} className="rounded-circle"
                            width="50" alt="User" />
                    </a>
                    <div className="media-body ml-3">
                        <span className="text-secondary">{message.creator_serializer.fullname}</span>
                        <small className="text-muted ml-2">{message.created_at}</small>
                        <div className="mt-3 font-size-sm">
                            <p>
                                {message.message}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

const TopicForm = ({createMessage}) => {
    const [messageInput, setmessageInput] = useState();

    return (
        <form method="post" onSubmit={(event) => {event.preventDefault(); createMessage(messageInput); setmessageInput("");}}>
            <div className="form-group mb-2">
                <label htmlFor="reply" className="">Your message</label>
                <textarea className="form-control" id="reply" name="message" style={{height: "145px"}} onChange={(event) => setmessageInput(event.target.value)} value={messageInput}></textarea>
            </div>
            <button type="submit" className="btn btn-primary mb-2">Send</button>
        </form>
    )
}

const TopicDetail = ({props}) => {
    const [filter, setFilter] = useState(props.filter || "all");
    const [search, setSearch] = useState(props.search || "");
    const [result, setResult] = useState();
    const [loading, setLoading] = useState(true);

    useEffect(async () => {
        await fetchTopicDetail()
        setLoading(false)
    }, []);
    
    useEffect(async () => {
        console.log(loading)
        if (!loading) window.location = `/topics/react/?search=${search}&filter=${filter}`
    }, [filter, search]);

    const fetchTopicDetail = async (url=null) => {
        const fetchUrl = `/api/topic/${props.topicid}/`;
        const response = await jsonFetchData(fetchUrl);
        setResult(response)
    }

    const createMessage = async (message) => {
        const fetchUrl = `/api/topic/${props.topicid}/message/`;
        const response = await jsonFetchData(fetchUrl, "POST", {message: message});
        setResult({...result, messages_serializer:  [...result.messages_serializer, response]})
    }

    return (
        <div className="inner-wrapper">
            <TopicSideBar filter={filter} search={search} setFilter={setFilter}/>

            <div className="inner-main">
                <TopicHeader filter={filter} search={search} setSearch={setSearch} />
                { result && (
                    <div className="inner-main-body p-2 p-sm-3 forum-content">
                        <a onClick={() => window.history.back()} className="btn btn-light btn-sm mb-3 has-icon">
                            <i className="fa fa-arrow-left mr-2"></i> Back
                        </a>

                        <div className="card">
                            <div className="card-body">
                                <div className="media forum-item">
                                    <div className="card-link">
                                        <img src={result.creator_serializer.avatar_url} className="rounded-circle"
                                            width="50" alt="User" />
                                    </div>
                                    <div className="media-body ml-3">
                                        <span className="text-secondary">{result.creator_serializer.fullname}</span>
                                        <small className="text-muted ml-2">{result.created_at}</small>
                                        <h5 className="mt-1">{result.title}</h5>
                                        <div className="mt-3 font-size-sm">
                                            <p>
                                                {result.description}
                                            </p>
                                        </div>
                                    </div>
                                    <div className="text-muted small text-center">
                                        <span><i className="far fa-comment ml-2"></i> {result.topicmessage_count}</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <hr />

                        {result.messages_serializer.map(message => <TopicMessage key={`message-${message.pk}`} message={message} />)}
                        <hr />

                        <TopicForm createMessage={createMessage} />
                    </div>
                )}
            </div>
        </div>
    )
}

export default TopicDetail